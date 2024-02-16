# Import standard library
import sys
from functools import partial, reduce
from json import load
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pygame
from tqdm import tqdm

from utility import *

# TODO update readme file

# ! The creation of new bodies is boring and tedious

# ! Constants should be more

# TODO merge bodies when they collide


# calculates the gravitational field generated by a mass at a distance
def calc_gravitational_acceleration(
    mass: float, pos: Vector2D, oth_pos: Vector2D
) -> Vector2D:
    distance = calc_distance(pos, oth_pos)
    theta = (oth_pos - pos).angle()
    return Vec2D_from_polar(const.G * mass / (distance**2), theta)


# calcolate the distance of two bodies
def calc_distance(pos1: Vector2D, pos2: Vector2D) -> float:
    return (pos1 - pos2).mod()


# Calculate the acceleration effect of oth_body on body
def add_object_field(sum: Vector2D, oth_body: Body, body: Body) -> Vector2D:
    # ! this if to remove the error of .angle() if the vector is a zero
    # ! it should be removed after the implementation of merging
    if oth_body.pos == body.pos:
        return sum

    return sum + calc_gravitational_acceleration(
        mass=oth_body.mass, pos=body.pos, oth_pos=oth_body.pos
    )


# Calculate the effect of all other bodies on the singular body
def calculate_object_acceleration(body: Body, oth_bodies: Tuple[Body, ...]) -> Vector2D:
    # * setting add_object_field on to obj
    func_add = partial(add_object_field, body=body)
    return reduce(func_add, oth_bodies, Vector2D(0, 0))


# Calculate and set the effect of ALL objects on each other
def calculate_objects_accelerations(*all_objs: Tuple[Body, ...]) -> None:
    # * calculate the acceleration for each body
    accelerations = [Vector2D(0, 0) for i in all_objs]
    for i, obj in enumerate(all_objs):
        oth_objs = [oth_obj for oth_obj in all_objs if oth_obj != obj]
        accelerations[i] = calculate_object_acceleration(obj, oth_objs)

    # * after having calculated all accelerations change the position and velocity
    for obj, acc in zip(all_objs, accelerations):
        obj.accelerate(acc)


def main() -> None:
    from utility.bodies import Bodies

    with open("Settings.json", "r") as f:
        config = load(f)
    dt = config["dt"]

    """
    interval = 25
    iters = 20000
    print(f"The simulation will last {interval*iters*dt /(60*60*24*365):.4g} years")

    test_accuracy(*Bodies, interval=interval, iterations=iters)
    """

    print(Bodies)
    run_simulation(*Bodies, dt=dt)

    return None


def test_accuracy(
    *Bodies: Tuple[Body, ...], interval: int = 1000, iterations: int = 1000
) -> None:

    errors = {
        "mechanical_en": np.zeros(iterations + 1),
        "kinetic_en": np.zeros(iterations + 1),
        "potential_en": np.zeros(iterations + 1),
        "momentum": np.zeros(iterations + 1),
    }

    for iter in tqdm(range(iterations)):
        mec, kin, pot = energy_error(*Bodies)
        errors["mechanical_en"][iter] = mec
        errors["kinetic_en"][iter] = kin
        errors["potential_en"][iter] = pot
        errors["momentum"][iter] = momentum_error(*Bodies)

        for _ in range(interval):
            calculate_objects_accelerations(*Bodies)
    else:
        mec, kin, pot = energy_error(*Bodies)
        errors["mechanical_en"][iterations] = mec
        errors["kinetic_en"][iterations] = kin
        errors["potential_en"][iterations] = pot
        errors["momentum"][iterations] = momentum_error(*Bodies)

    x = np.arange(0, iterations + 1)
    max_mec_en = max(np.fabs(errors["mechanical_en"]))
    errors["mechanical_en"] /= max_mec_en
    errors["kinetic_en"] /= max_mec_en
    errors["potential_en"] /= max_mec_en

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(16, 4))

    ax1.plot(x, errors["mechanical_en"])
    ax1.title.set_text("Mechanical Energy")
    ax2.plot(x, errors["kinetic_en"])
    ax2.title.set_text("Kinetic Energy")
    ax3.plot(x, errors["potential_en"])
    ax3.title.set_text("Potential Energy")
    ax4.plot(x, errors["momentum"])
    ax4.title.set_text("Momentum")

    plt.suptitle("Errors in Energy")
    ax1.text(
        0.9,
        0.1,
        f"Normalized to {max_mec_en:.2e}J",
        horizontalalignment="right",
        verticalalignment="center",
        transform=ax1.transAxes,
        color="green",
    )
    ax2.text(
        0.9,
        0.1,
        f"Normalized to {max_mec_en:.2e}J",
        horizontalalignment="right",
        verticalalignment="center",
        transform=ax2.transAxes,
        color="green",
    )
    ax3.text(
        0.9,
        0.1,
        f"Normalized to {max_mec_en:.2e}J",
        horizontalalignment="right",
        verticalalignment="center",
        transform=ax3.transAxes,
        color="green",
    )
    plt.show()


def energy_error(*bodies: Body) -> Tuple[float, ...]:
    kinetic = get_kinetic_err(bodies)
    potential = get_potential_err(bodies)
    mechanical = kinetic + potential
    return mechanical, kinetic, potential


def get_kinetic_err(bodies: Tuple[Body, ...]) -> float:
    kinetic = 0
    for body in bodies:
        kinetic += 1 / 2 * body.mass * body.vel.mod() ** 2
    return kinetic


def get_potential_err(bodies: Tuple[Body, ...]) -> float:
    potential = 0
    for body in bodies:
        for oth_body in bodies:
            if oth_body == body:
                continue

            potential -= (
                const.G
                * body.mass
                * oth_body.mass
                / calc_distance(body.pos, oth_body.pos)
            )
    return potential


def momentum_error(*bodies: Tuple[Body, ...]) -> float:
    momentum = Vector2D(0, 0)
    for body in bodies:
        momentum += body.mass * body.vel
    return momentum.mod()


def run_simulation(*bodies: Tuple[Body, ...], dt: float) -> None:
    # Setup
    WIDTH, HEIGHT = 800, 800
    CENTERX, CENTERY = WIDTH // 2, HEIGHT // 2

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def draw():
        for body in bodies:
            xpos, ypos = body.pos.get_cart_coord()
            xpos, ypos = (
                xpos * CENTERX / const.NEPTUNE_D + CENTERX,
                ypos * CENTERY / const.NEPTUNE_D + CENTERY,
            )
            pygame.draw.circle(screen, WHITE, (xpos, ypos), 3)

    doLoop = True
    while doLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    doLoop = False

        screen.fill(BLACK)
        calculate_objects_accelerations(*bodies)
        draw()
        pygame.time.Clock().tick(60)

        pygame.display.update()

    return None


if __name__ == "__main__":
    main()
