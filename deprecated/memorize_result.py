from functools import reduce
from typing import Tuple

from ..utility.bodyclass import Body
from ..utility.mycostants import Constants as const

def memorize_result(just_last = True):
    def decorator(func):
        __cache = {}

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if func.__name__ not in __cache:
                __cache[func.__name__] = {1 : result}
            else:
                __cache[func.__name__][max(__cache.keys()) +1] = result

            if just_last:
                return result

            return __cache

        return wrapper

    return decorator

@memorize_result(just_last=False)
def mechanical_error(*Bodies : Tuple[Body]) -> Tuple[float]:
    return kinetic_error(Bodies) + potential_error(Bodies)

@memorize_result
def kinetic_error(Bodies):
    kinetic = 0
    for body in Bodies:
        kinetic += 1/2 * body.mass * body.vel.mod()**2
    return kinetic

@memorize_result
def potential_error(Bodies):
    potential = 0
    for body in Bodies:
        for oth_body in Bodies:
            if oth_body == body:
                continue

            potential -= const.G * body.mass * oth_body.mass / distance(body, oth_body)
    return potential

def distance(body, oth_body):
    return (body.pos - oth_body.pos).mod()
