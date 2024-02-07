from json import load
from os import path
from typing import Tuple

from .vectors2D import Vector2D

with open(path.abspath("Settings.json"), "r") as f:
    config = load(f)
dt = config["dt"]


class Body:
    """Body class stores the information of a celestial body and has the modules
    for the first order Euler's method for computing a physical system
    """

    def __init__(
        self,
        name: str,
        mass: float,
        x_pos: float,
        y_pos: float,
        x_vel: float,
        y_vel: float,
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
        # ? I could add a type variable that indicates the type of stellar object it is

        self.pos = Vector2D(x_pos, y_pos)  # Position vector
        self.vel = Vector2D(x_vel, y_vel)  # Velocity vector

    def __str__(self) -> str:
        """Returns:
        str: Description of the object in cartesian coordinates with
        """
        return (
            f"The body {self.name}:\n"
            + "\tCartesian position is     "
            + f"({self.pos.x:.3g}m,     {self.pos.y:.3g}m).\n"
            + "\tCartesian velocity is     "
            + f"({self.vel.x:.3g}m/s,   {self.vel.y:.3g}m/s).\n"
        )

    def __repr__(self) -> str:
        return f"{self.name}, {self.pos.mod():.5g}, {self.vel.mod():.5g}"

    def __eq__(self, other: object) -> bool:
        """
        Parameters
        ----------
        other : object
            another body

        Returns
        -------
        bool
            True if self and other have the same name
        """
        return bool(self.name == other.name)

    def accelerate(self, acceleration: Vector2D) -> None:
        """accelerate and move the body

        It uses second order euler's method to calculate an iteration

        Parameters
        ----------
        acceleration : Vector2D
            The current acceleration vector
        """
        self.vel += acceleration * dt
        self.pos += self.vel * dt
