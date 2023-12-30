from math import cos, sin, pi
from typing import Tuple

from .Simulation import Body, createPosition
from .utility import const

def createPosition(mod, vmod, angle) -> Tuple[float]:
    x = mod * cos(angle)
    y = mod * sin(angle)
    
    vx = vmod * cos(angle + pi/2)
    vy = vmod * sin(angle + pi/2)
    
    return x, y, vx, vy

body1 = Body("Sole",    const.SUN_M,     *createPosition(0, 0, 0))
body2 = Body("Mercurio",const.MERCURY_M, *createPosition(const.MERCURY_D, const.MERCURY_V,  0.1))
body3 = Body("Venere",  const.VENUS_M,   *createPosition(const.VENUS_D,   const.VENUS_V,    3))
body4 = Body("Terra",   const.EARTH_M,   *createPosition(const.EARTH_D,   const.EARTH_V,    1.5))
body5 = Body("Marte",   const.MARS_M,    *createPosition(const.MARS_D,    const.MARS_V,     4.4))
body6 = Body("Giove",   const.JUPITER_M, *createPosition(const.JUPITER_D, const.JUPITER_V,  0.7))
body7 = Body("Saturno", const.SATURN_M,  *createPosition(const.SATURN_D,  const.SATURN_V,   6))
body8 = Body("Urano",   const.URANUS_M,  *createPosition(const.URANUS_D,  const.URANUS_V,   0.8))
body9 = Body("Nettuno", const.NEPTUNE_M, *createPosition(const.NEPTUNE_D, const.NEPTUNE_V,  6.1))

Bodies = (body1, body2, body3, body4, body5, body6, body7, body8, body9)