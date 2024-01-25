from typing import Tuple
from os import path

import json

from .vectors2D import Vector2D

with open(path.abspath("Settings.json"), "r") as f:
    config = json.load(f)
dt = config["dt"]

class Body:
    """Body class stores the information of a celestial body and has the modules
    for the first order Euler's method for computing a physical system
    """
    def __init__(self, name : str, mass: float,
                 x_pos: float, y_pos: float,
                 x_vel: float, y_vel: float
                 ) -> None:
        """Initialize the Body

        Args:
            name (str): Name of the body
            mass (float): Mass of the Body
            x_pos (float): x coordinate of the position vector
            y_pos (float): y coordinate of the position vector
            x_vel (float): x coordinate of the velocity vector
            y_vel (float): y coordinate of the velocity vector
        """

        self.name = name
        self.mass = mass
        # ? I could add the object radius for a merge implementation

        self.pos = Vector2D(x_pos, y_pos) # Position vector
        self.vel = Vector2D(x_vel, y_vel) # Velocity vector

    def __str__(self) -> str:
        """Returns:
            str: Description of the object in cartesian coordinates with
        """
        return f"The body {self.name}:\n"\
            + "\tCartesian position is     "\
                + f"({self.pos.x:.3g}m,     {self.pos.y:.3g}m).\n"\
            + "\tCartesian velocity is     "\
                + f"({self.vel.x:.3g}m/s,   {self.vel.y:.3g}m/s).\n"

    #Return all available information in a str[tuple]
    def __repr__(self) -> str:
        return f"{self.name}, {self.pos.mod():.5g}, {self.vel.mod():.5g}"

    def __eq__(self, other: object) -> bool:
        """Args:
            other (object): another body

        Returns:
            bool: true if the objects have the same name
        """
        if self.name == other.name:
            return True
        return False

    # TODO put this function as "private" to not be called externally
    def move(self) -> None:
        self.pos += self.vel * dt

    def accelerate(self, acceleration : Vector2D) -> None:
        self.vel += acceleration * dt
        self.move()
