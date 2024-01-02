#Import standard library
import math
from typing import Tuple
from functools import partial, reduce

import numpy as np
import matplotlib.pyplot as plt

from utility import Vector2D, const, Body

from pprint import pprint

# ! The program is not slow, but it's neither fast.
# ! A big improvement can still be made

# ! The creation of new bodies is boring and tedious

# ! Constants should be more accurate

# TODO the doc_strings of everything I haven't done (it's a lot)

def calc_gravitational_acceleration(mass : float, distance : float) -> float:
    return const.G*mass/(distance**2)

def calc_distance(pos1 : Vector2D, pos2 : Vector2D) -> float:
    return (pos1-pos2).mod()

# Calculate the effect of the body oth_obj on obj
def add_object_field(sum : Vector2D, oth_obj : Body, obj : Body) -> Vector2D:
    mod_accel = calc_gravitational_acceleration(mass = oth_obj.mass,
                                                distance = calc_distance(obj.pos, oth_obj.pos))
    theta = (obj.pos - oth_obj.pos).angle() + math.pi
    return sum + Vector2D(mod_accel * math.cos(theta), mod_accel * math.sin(theta))

# Calculate the effect of the all oth_objs on the singular obj
def calculate_object_acceleration(obj : Body, oth_objs : Tuple[Body]) -> Vector2D:
    # * setting add_object_field on to obj
    func_add = partial(add_object_field, obj=obj)
    return reduce(func_add, oth_objs, Vector2D(0, 0))

# Calculate and set the effect of ALL objects on each other
def calculate_objects_accelerations(*all_objs : Tuple[Body]) -> None:
    # Calculate the accelerations of each object
    accelerations = [Vector2D(0, 0) for i in all_objs]
    for i, obj in enumerate(all_objs):
        oth_objs = [oth_obj for oth_obj in all_objs if oth_obj != obj]
        accelerations[i] = calculate_object_acceleration(obj, oth_objs)

    for obj, acc in zip(all_objs, accelerations):
        obj.set_acceleration(acc)



def main():
    from utility.bodies import Bodies

    test_accuracy(*Bodies[:4])

    return None



def test_accuracy(*Bodies : Tuple[Body], interval : int = 100, iters : int = 1000) -> None:
    """Calculate and plot the distance from the Sun(first body),
        to the n-th body, over a period of time.
        The time period is calculated as T = dt * interval * iters.
        In the plot are shown iters x-values.
        The y-values are normalized to the maximum distance occurred during
        during the time period.

    Args:
        interval (int, optional): The interval of dt from an iteration to the
            other. Defaults to 100.
        iters (int, optional): The number of iterations. Defaults to 1000.
        NOTE the actual number of iteration of the method is interval*iters,
            iters it's just for reducing the number of points for the plot

    Returns:
        None
    """
    errors = [[0 for j in range(iters)] for i in Bodies]

    for iter in range(iters):
        for i in range(interval):
            calculate_objects_accelerations(*Bodies)

        errs = [(body.pos-Bodies[0].pos).mod() for body in Bodies]
        for i, err in enumerate(errs):
            errors[i][iter] = err

    x = np.arange(0, iters)
    errors = np.array(errors)

    maxValues = []
    for i, body in enumerate(Bodies):
        max_ = np.max(errors[i])

        if max_ == 0:
            maxValues.append(0)
            continue

        errors[i] /= max_
        maxValues.append(max_)

    fig, ax = plt.subplots()

    def filter_func(values : zip) -> bool:
        Body, error, max_ = values
        if max_ == 0:
            return False
        return True

    # * Plot each body that does not have error 0, x-ax are the n-th iteration,
    # * y-ax are the normalized errors
    for body, error, max_ in filter(filter_func, zip(Bodies, errors, maxValues)):
        ax.plot(x, error, label=f'{body.name}: {max_:.3e}')

    ax.legend()
    plt.show()



if __name__ == "__main__":
    main()