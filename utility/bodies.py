from math import cos, pi, sin
from typing import Tuple

from .bodyclass import Body
from .mycostants import Constants as const


def create_position(
    mod: float, v_mod: float, angle: float, v_angle: float
) -> Tuple[float, float, float, float]:
    """Generate the position and velocity of a vector

    Args:
        mod (float): Module of the position vector
        v_mod (float): Module of the velocity vector
        angle (float): angle of the position vector
        v_angle (float): angle of the velocity vector

    Returns:
        Tuple[float]:
            x (float): the x coordinate of the position of the body
            y (float): the y coordinate of the position of the body
            vx (float): the x coordinate of the velocity of the body
            vy (float): the y coordinate of the velocity of the body
    """
    x = mod * cos(angle)
    y = mod * sin(angle)

    vx = v_mod * cos(v_angle)
    vy = v_mod * sin(v_angle)

    return x, y, vx, vy


def get_perpendicular(angle: float, positive: bool = True) -> float:
    """Get the angle perpendicular

    Args:
        angle (float): the angle to set perpendicular to
        positive (bool, optional): whether the angle should be positive
            or negative. Defaults to True.

    Returns:
        float: the perpendicular to @angle (positive or negative)
    """
    if positive:
        return angle + pi / 2
    return angle - pi / 2


"""Here you can find default bodies

You can generate new bodies with:
Body(
    name (str): the name of the body
    mass (float): the mass of the body
    x_pos (float): the x coordinate of the position of the body
    y_pos (float): the y coordinate of the position of the body
    x_vel (float): the x coordinate of the velocity of the body
    y_vel (float): the y coordinate of the velocity of the body
)
or you can use Body(name, mass, create_position(mod, alpha, vel, beta))
"""
# ? for the creation of bodies I could use a better method: I still have to think about it
body1: Body = Body("Sole", const.SUN_M, *create_position(0, 0, 0, get_perpendicular(0)))
body2: Body = Body(
    "Mercurio",
    const.MERCURY_M,
    *create_position(const.MERCURY_D, const.MERCURY_V, 0.1, get_perpendicular(0.1))
)
body3: Body = Body(
    "Venere",
    const.VENUS_M,
    *create_position(const.VENUS_D, const.VENUS_V, 3, get_perpendicular(3))
)
body4: Body = Body(
    "Terra",
    const.EARTH_M,
    *create_position(const.EARTH_D, const.EARTH_V, 1.5, get_perpendicular(1.5))
)
body5: Body = Body(
    "Marte",
    const.MARS_M,
    *create_position(const.MARS_D, const.MARS_V, 4.4, get_perpendicular(4.4))
)
body6: Body = Body(
    "Giove",
    const.JUPITER_M,
    *create_position(const.JUPITER_D, const.JUPITER_V, 0.7, get_perpendicular(0.7))
)
body7: Body = Body(
    "Saturno",
    const.SATURN_M,
    *create_position(const.SATURN_D, const.SATURN_V, 6, get_perpendicular(6))
)
body8: Body = Body(
    "Urano",
    const.URANUS_M,
    *create_position(const.URANUS_D, const.URANUS_V, 0.8, get_perpendicular(0.8))
)
body9: Body = Body(
    "Nettuno",
    const.NEPTUNE_M,
    *create_position(const.NEPTUNE_D, const.NEPTUNE_V, 6.1, get_perpendicular(6.1))
)

# * Get the list of Bodies, you can also use other lists
Bodies: Tuple[Body] = (body1, body2, body3, body4, body5, body6, body7, body8, body9)
