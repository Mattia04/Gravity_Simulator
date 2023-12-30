#Import standard library
import math
from typing import Tuple
from functools import partial, reduce

import numpy as np
import matplotlib.pyplot as plt

from utility import Vector2D, const, Body

#Define time delta in s
dt = 60*60

#NOTE il programma è molto lento, aumentando dt si perde precisione, aumentando il framerate non cambia quasi nulla,\
#probabilmente c'è una funzione che impiega troppo tempo, dovrei controllare con i decorators
#NOTE NOTE ho controllato con i decoratori e non sembra essere python il problema
#NOTE la creazione di un body è una rottura di coglioni
#NOTE le costanti hanno nomi troppo lunghi

def calc_gravitational_acceleration(m : float, r : float) -> float:
    return const.G*m/(r**2)

def calc_dist(pos1 : Vector2D, pos2 : Vector2D) -> float:
    return (pos1-pos2).mod()
    
def addAccObj(sum : Vector2D, oth_obj : Body, obj : Body) -> Vector2D:
    mod_accel = calc_gravitational_acceleration(m=oth_obj.mass, r=calc_dist(obj.pos, oth_obj.pos))
    theta = (obj.pos - oth_obj.pos).angle() + math.pi
    return sum + Vector2D(mod_accel * math.cos(theta), mod_accel * math.sin(theta))

def calcAccObj(obj : Body, oth_objs : Tuple[Body]) -> None:
    func_add = partial(addAccObj, obj=obj)
    return reduce(func_add, oth_objs, Vector2D(0, 0))

def calcAccAllObj(*all_objs : Tuple[Body]) -> None:
    accelerations = [Vector2D(0, 0) for i in all_objs]
    for i, obj in enumerate(all_objs):
        oth_objs = [oth_obj for oth_obj in all_objs if oth_obj != obj]
        accelerations[i] = calcAccObj(obj, oth_objs)
    for obj, acc in zip(all_objs, accelerations):
        obj.setAcceleration(acc)


    
def main():
    from utility.bodies import Bodies
    
    test_accuracy(Bodies[:6])
    
    return None



def test_accuracy(*Bodies : Tuple[Body], interval : int = 1000, iters : int = 1000) -> None:
    errors = [[0 for j in range(iters)] for i in Bodies]
    
    for iter in range(iters):
        for i in range(interval):
            calcAccAllObj(*Bodies)
            
        errs = [(body.pos-Bodies[0].pos).mod() for body in Bodies]
        for i, err in enumerate(errs):        
            errors[i][iter] = err
    
    x = np.arange(0, iters)
    errors = np.array(errors)
    
    maxValues = []
    for i, body in enumerate(Bodies):
        max = np.max(errors[i])
        errors[i] /= max
        maxValues.append(max)
    
    fig, ax = plt.subplots()
    for i, body in enumerate(Bodies):
        ax.plot(x, errors[i], label=f'{body.name}: {maxValues[i]:.3e}')
    
    ax.legend()
    plt.show()



if __name__ == "__main__":
    main()