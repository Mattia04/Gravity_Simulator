from math import cos, sin, pi
from typing import Tuple

from .bodyclass import Body
from .mycostants import Constants as const

def createPosition(mod : float, v_mod : float, angle : float) -> Tuple[float]:
    x = mod * cos(angle)
    y = mod * sin(angle)

    vx = v_mod * cos(angle + pi/2)
    vy = v_mod * sin(angle + pi/2)

    return x, y, vx, vy

body1 : Body = Body("Sole",    const.SUN_M,     *createPosition(0, 0, 0))
body2 : Body = Body("Mercurio",const.MERCURY_M, *createPosition(const.MERCURY_D, const.MERCURY_V,  0.1))
body3 : Body = Body("Venere",  const.VENUS_M,   *createPosition(const.VENUS_D,   const.VENUS_V,    3))
body4 : Body = Body("Terra",   const.EARTH_M,   *createPosition(const.EARTH_D,   const.EARTH_V,    1.5))
body5 : Body = Body("Marte",   const.MARS_M,    *createPosition(const.MARS_D,    const.MARS_V,     4.4))
body6 : Body = Body("Giove",   const.JUPITER_M, *createPosition(const.JUPITER_D, const.JUPITER_V,  0.7))
body7 : Body = Body("Saturno", const.SATURN_M,  *createPosition(const.SATURN_D,  const.SATURN_V,   6))
body8 : Body = Body("Urano",   const.URANUS_M,  *createPosition(const.URANUS_D,  const.URANUS_V,   0.8))
body9 : Body = Body("Nettuno", const.NEPTUNE_M, *createPosition(const.NEPTUNE_D, const.NEPTUNE_V,  6.1))

Bodies : Tuple[Body] = (body1, body2, body3, body4, body5, body6, body7, body8, body9)