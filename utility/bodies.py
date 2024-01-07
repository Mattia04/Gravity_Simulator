from math import cos, sin, pi
from typing import Tuple

from .bodyclass import Body
from .mycostants import Constants as const

def create_position(mod : float, v_mod : float, angle : float, v_angle : float) -> Tuple[float]:
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

def get_perpendicular(angle : float, positive : bool = True) -> float:
    """Get the angle perpendicular

    Args:
        angle (float): the angle to set perpendicular to
        positive (bool, optional): whether the angle should be positive
            or negative. Defaults to True.

    Returns:
        float: the perpendicular to @angle (positive or negative)
    """
    if positive:
        return angle + pi/2
    return angle - pi/2

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
body1 : Body = Body("Sole",    const.SUN_M,     *create_position(0,               0,                0,      get_perpendicular(0)))
body2 : Body = Body("Mercurio",const.MERCURY_M, *create_position(const.MERCURY_D, const.MERCURY_V,  0,      get_perpendicular(0)))
body3 : Body = Body("Venere",  const.VENUS_M,   *create_position(const.VENUS_D,   const.VENUS_V,    0,      get_perpendicular(0)))
body4 : Body = Body("Terra",   const.EARTH_M,   *create_position(const.EARTH_D,   const.EARTH_V,    0,      get_perpendicular(0)))
body5 : Body = Body("Marte",   const.MARS_M,    *create_position(const.MARS_D,    const.MARS_V,     0,      get_perpendicular(0)))
body6 : Body = Body("Giove",   const.JUPITER_M, *create_position(const.JUPITER_D, const.JUPITER_V,  0,      get_perpendicular(0)))
body7 : Body = Body("Saturno", const.SATURN_M,  *create_position(const.SATURN_D,  const.SATURN_V,   0,      get_perpendicular(0)))
body8 : Body = Body("Urano",   const.URANUS_M,  *create_position(const.URANUS_D,  const.URANUS_V,   0,      get_perpendicular(0)))
body9 : Body = Body("Nettuno", const.NEPTUNE_M, *create_position(const.NEPTUNE_D, const.NEPTUNE_V,  0,      get_perpendicular(0)))
# ! this was the fastest way to get more bodies
body21 : Body = Body("Mercurio",const.MERCURY_M, *create_position(const.MERCURY_D, const.MERCURY_V,  1*pi/4,      get_perpendicular(1*pi/4)))
body22 : Body = Body("Mercurio",const.MERCURY_M, *create_position(const.MERCURY_D, const.MERCURY_V,  2*pi/4,      get_perpendicular(2*pi/4)))
body23 : Body = Body("Mercurio",const.MERCURY_M, *create_position(const.MERCURY_D, const.MERCURY_V,  3*pi/4,      get_perpendicular(3*pi/4)))
body31 : Body = Body("Venere",  const.VENUS_M,   *create_position(const.VENUS_D,   const.VENUS_V,    1*pi/4,      get_perpendicular(1*pi/4)))
body32 : Body = Body("Venere",  const.VENUS_M,   *create_position(const.VENUS_D,   const.VENUS_V,    2*pi/4,      get_perpendicular(2*pi/4)))
body33 : Body = Body("Venere",  const.VENUS_M,   *create_position(const.VENUS_D,   const.VENUS_V,    3*pi/4,      get_perpendicular(3*pi/4)))
body41 : Body = Body("Terra",   const.EARTH_M,   *create_position(const.EARTH_D,   const.EARTH_V,    1*pi/4,      get_perpendicular(1*pi/4)))
body42 : Body = Body("Terra",   const.EARTH_M,   *create_position(const.EARTH_D,   const.EARTH_V,    2*pi/4,      get_perpendicular(2*pi/4)))
body43 : Body = Body("Terra",   const.EARTH_M,   *create_position(const.EARTH_D,   const.EARTH_V,    3*pi/4,      get_perpendicular(3*pi/4)))
body51 : Body = Body("Marte",   const.MARS_M,    *create_position(const.MARS_D,    const.MARS_V,     1*pi/4,      get_perpendicular(1*pi/4)))
body52 : Body = Body("Marte",   const.MARS_M,    *create_position(const.MARS_D,    const.MARS_V,     2*pi/4,      get_perpendicular(2*pi/4)))
body53 : Body = Body("Marte",   const.MARS_M,    *create_position(const.MARS_D,    const.MARS_V,     3*pi/4,      get_perpendicular(3*pi/4)))
body61 : Body = Body("Giove",   const.JUPITER_M, *create_position(const.JUPITER_D, const.JUPITER_V,  1*pi/4,      get_perpendicular(1*pi/4)))
body62 : Body = Body("Giove",   const.JUPITER_M, *create_position(const.JUPITER_D, const.JUPITER_V,  2*pi/4,      get_perpendicular(2*pi/4)))
body63 : Body = Body("Giove",   const.JUPITER_M, *create_position(const.JUPITER_D, const.JUPITER_V,  3*pi/4,      get_perpendicular(3*pi/4)))
body71 : Body = Body("Saturno", const.SATURN_M,  *create_position(const.SATURN_D,  const.SATURN_V,   1*pi/4,      get_perpendicular(1*pi/4)))
body72 : Body = Body("Saturno", const.SATURN_M,  *create_position(const.SATURN_D,  const.SATURN_V,   2*pi/4,      get_perpendicular(2*pi/4)))
body73 : Body = Body("Saturno", const.SATURN_M,  *create_position(const.SATURN_D,  const.SATURN_V,   3*pi/4,      get_perpendicular(3*pi/4)))
body81 : Body = Body("Urano",   const.URANUS_M,  *create_position(const.URANUS_D,  const.URANUS_V,   1*pi/4,      get_perpendicular(1*pi/4)))
body82 : Body = Body("Urano",   const.URANUS_M,  *create_position(const.URANUS_D,  const.URANUS_V,   2*pi/4,      get_perpendicular(2*pi/4)))
body83 : Body = Body("Urano",   const.URANUS_M,  *create_position(const.URANUS_D,  const.URANUS_V,   3*pi/4,      get_perpendicular(3*pi/4)))
body91 : Body = Body("Nettuno", const.NEPTUNE_M, *create_position(const.NEPTUNE_D, const.NEPTUNE_V,  1*pi/4,      get_perpendicular(1*pi/4)))
body92 : Body = Body("Nettuno", const.NEPTUNE_M, *create_position(const.NEPTUNE_D, const.NEPTUNE_V,  2*pi/4,      get_perpendicular(2*pi/4)))
body93 : Body = Body("Nettuno", const.NEPTUNE_M, *create_position(const.NEPTUNE_D, const.NEPTUNE_V,  3*pi/4,      get_perpendicular(3*pi/4)))

# * Get the list of Bodies, you can also use other lists
Bodies : Tuple[Body] = (body1, body2, body3, body4, body5, body6, body7, body8, body9,
                        body21, body22, body23,
                        body31, body32, body33,
                        body41, body42, body43,
                        body51, body52, body53,
                        body61, body62, body63,
                        body71, body72, body73,
                        body81, body82, body83,
                        body91, body92, body93)