from typing import Tuple
from os import path

import json

from .vectors2D import Vector2D

with open(path.abspath("Settings.json"), "r") as f:
    config = json.load(f)
dt = config["dt"]

# TODO write docstring
# TODO change function names to be in line with PEP8
class Body:
    def __init__(self, name : str, mass: float,
                 x_pos: float, y_pos: float,
                 x_vel: float, y_vel: float
                 ) -> None:

        self.name = name # Name of the Body
        self.mass = mass # Mass of the Body

        self.pos = Vector2D(x_pos, y_pos) # Position vector
        self.vel = Vector2D(x_vel, y_vel) # Velocity vector
        # For now it's initialized at zero, because it will be calculated later
        self.acc = Vector2D(0, 0) # Acceleration vector

    # Returns the available information in cartesian coordinates
    def __str__(self) -> str:
        return f"The body {self.name}:\n"\
            + "\tCartesian position is     "\
                + f"({self.pos.x:.3g}m,     {self.pos.y:.3g}m).\n"\
            + "\tCartesian velocity is     "\
                + f"({self.vel.x:.3g}m/s,   {self.vel.y:.3g}m/s).\n"\
            + "\tCartesian acceleration is "\
                + f"({self.acc.x:.3g}m/s^2, {self.acc.y:.3g}m/s^2)"

    #Return all available information in a str[tuple]
    def __repr__(self) -> str:
        return f"{self.name}, {self.pos.mod():.5g}, \
            {self.vel.mod():.5g}, {self.acc.mod():.5g}"

    #Set equivalence by name
    def __eq__(self, other: object) -> bool:
        if self.name == other.name:
            return True
        return False

    # ! note that == and < are not referring to the same thing
    # ! this is why I didn't add the other operations
    def __lt__(self, other: object) -> bool:
        if self.pos.mod() == other.pos.mod():
            return True
        return False

    # Move the object
    # * Using the first order Euler Method
    def move(self) -> None:
        self.pos += self.vel * dt

    #Change the velocity
    def accelerate(self) -> None:
        self.vel += self.acc * dt

    #Set the acceleration from external input
    def set_acceleration(self, other : Vector2D) -> None:
        self.acc = other
        self.accelerate()
        self.move()