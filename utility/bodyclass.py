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
        # ! For now it's initialized at zero, because it will be calculated later:
        # ? It could be not needed
        self.acc = Vector2D(0, 0) # Acceleration vector

    def __str__(self) -> str:
        """Returns:
            str: Description of the object in cartesian coordinates with
        """
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

    def __eq__(self, other: object) -> bool:
        """Args:
            other (object): another body

        Returns:
            bool: true if the objects have the same name
        """
        if self.name == other.name:
            return True
        return False

    def move(self) -> None:
        """Adds the first order approximation (velocity*time_delta) to
            the current position
        """
        self.pos += self.vel * dt
        # ? i have to figure out why i can't use 1/2 * acc * dt^2

    # ? to remove the self.acc I could pass here the acceleration vector
    def accelerate(self) -> None:
        """Adds the first order approximation (acceleration*time_delta) to
            the current velocity
        """
        self.vel += self.acc * dt
        # ? and add self.move()

    # ? and remove all this function
    def set_acceleration(self, other : Vector2D) -> None:
        """Set the current acceleration from external input and calculates the
            new velocity and position

        Args:
            other (Vector2D): The vector that describes the current acceleration
        """
        self.acc = other
        self.accelerate()
        self.move()
