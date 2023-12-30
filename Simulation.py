#Import my libraries
from utils import Vector2D, const
#import utils NOTE HOW CAN I FUCKING JUST DO THIS?

import math
from typing import Tuple
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from functools import partial, reduce

import pygame

#Define time delta in s
dt = 60*60

#NOTE il programma è molto lento, aumentando dt si perde precisione, aumentando il framerate non cambia quasi nulla,\
#probabilmente c'è una funzione che impiega troppo tempo, dovrei controllare con i decorators
#NOTE NOTE ho controllato con i decoratori e non sembra essere python il problema
#NOTE la creazione di un body è una rottura di coglioni
#NOTE le costanti hanno nomi troppo lunghi

class Body:
    def __init__(self, name : str, mass: float, x_pos: float, y_pos: float, x_vel: float, y_vel: float, size : int = 3, color : Tuple[int] = (0, 0, 0)):
        #Define the name of the object
        self.name = name
        #Define the mass of the object
        self.mass = mass
        
        #Vectors
        #Define the position vector
        self.pos = Vector2D(x_pos, y_pos)
        #Define the velocity vector
        self.vel = Vector2D(x_vel, y_vel)
        #Define the acceleration vector
        self.acc = Vector2D(0, 0)
        
        #For pygame
        #Define the color of the object
        self.size = size
        #Define the color of the object
        self.color = color
        
    #Return all available information, Cart = cartesian mode, Polr = polar mode
    def __str__(self, mode = "Short"):
        if mode == "Short":
            string = f"Il corpo {self.name}\n"\
                + f"Si trova nelle coordinate cartesiane ({self.pos.x:.3g}m, {self.pos.y:.3g}m).\n"\
                + f"Si muove con velocità cartesiane     ({self.vel.x:.3g}m/s, {self.vel.y:.3g}m/s).\n"
        elif mode == "Cart":
            string = f"Il corpo {self.name} di massa {self.mass:.3g}kg.\n"\
                + f"Si trova nelle coordinate cartesiane ({self.pos.x:.3g}m, {self.pos.y:.3g}m).\n"\
                + f"Si muove con velocità cartesiane ({self.vel.x:.3g}m/s, {self.vel.y:.3g}m/s).\n"\
                + f"Con accelerazione di  ({self.acc.x:.3g}m/s^2, {self.acc.y:.3g}m/s^2)"
        elif mode == "Polr":
            string = f"Il corpo {self.name} di massa {self.mass:.3g}kg.\n"\
                + f"Si trova in modulo {self.pos.mod:.3g}m ad un angolo {self.pos.angle:.3g} [rad].\n"\
                + f"Si muove con velocità di modulo {self.vel.mod:.3g}m ad un angolo {self.vel.angle:.3g} [rad].\n"\
                + f"Con accelerazione di modulo {self.acc.mod:.3g}m ad un angolo {self.acc.angle:.3g} [rad]"
        else:
            string = "Invalid mode"
        return string
    
    #Return all available information in a tuple
    def __repr__(self) -> str:
        return f"{self.name}, {self.pos.mod():.5g}, {self.vel.mod():.5g}, {self.acc.mod():.5g}"
    
    #Set equivalence by name
    def __eq__(self, __value: object) -> bool:
        if self.name == __value.name:
            return True
        else: 
            return False
    
    #Move the object
    def move(self) -> None:
        self.pos += self.vel * dt #+ 1/2 * self.acc * dt**2
    
    #Change the velocity
    def accelerate(self) -> None:
        self.vel += self.acc * dt
    
    #Set the acceleration from inputclear
    def setAcceleration(self, other : Vector2D) -> None:
        self.acc = other
        self.accelerate()
        self.move()
    
    def display(self, screen : pygame.display, scale_coord : float) -> None:
        def coords(pos : Vector2D) -> Tuple[float]:
            x_, y_ = screen.get_size()
            return (pos.x/(scale_coord/x_*2) + x_//2, -pos.y/(scale_coord/y_*2) + y_//2)
        
        pygame.draw.circle(screen, color=self.color, center=(coords(self.pos)), radius=self.size, width=self.size)

def calc_acc_grav(m : float, r : float) -> float:
    return const.G*m/(r**2)

def calc_dist(pos1 : Vector2D, pos2 : Vector2D) -> float:
    return (pos1-pos2).mod()
    
def addAccObj(sum : Vector2D, oth_obj : Body, obj : Body) -> Vector2D:
    mod_accel = calc_acc_grav(m=oth_obj.mass, r=calc_dist(obj.pos, oth_obj.pos))
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
    body1 = Body("Sole",    const.SUN_MASS,     *createPosition(0, 0, 0),                                       size=15, color=(255, 255, 0))
    body2 = Body("Mercurio",const.MERCURY_MASS, *createPosition(const.MERCURY_DIST, const.MERCURY_VEL,  0.1),   size=2,  color=(128, 128, 128))
    body3 = Body("Venere",  const.VENUS_MASS,   *createPosition(const.VENUS_DIST,   const.VENUS_VEL,    3),     size=3,  color=(192, 192, 0))
    body4 = Body("Terra",   const.EARTH_MASS,   *createPosition(const.EARTH_DIST,   const.EARTH_VEL,    1.5),   size=4,  color=(0, 0, 255))
    body5 = Body("Marte",   const.MARS_MASS,    *createPosition(const.MARS_DIST,    const.MARS_VEL,     4.4),   size=3,  color=(255, 0, 0))
    body6 = Body("Giove",   const.JUPITER_MASS, *createPosition(const.JUPITER_DIST, const.JUPITER_VEL,  0.7),   size=9,  color=(128, 64, 0))
    body7 = Body("Saturno", const.SATURN_MASS,  *createPosition(const.SATURN_DIST,  const.SATURN_VEL,   6),     size=8,  color=(128, 128, 0))
    body8 = Body("Urano",   const.URANUS_MASS,  *createPosition(const.URANUS_DIST,  const.URANUS_VEL,   0.8),   size=7,  color=(0, 0, 192))
    body9 = Body("Nettuno", const.NEPTUNE_MASS, *createPosition(const.NEPTUNE_DIST, const.NEPTUNE_VEL,  6.1),   size=6,  color=(0, 0, 128))
    
    test_accuracy(body1, body2, body3, body4, body5, body6)
    
    #pygame_animation(body1, body2, body3, body4, body5, body6, body7, body8, body9)
    return None

def createPosition(mod, vmod, angle) -> Tuple[float]:
    x = mod * math.cos(angle)
    y = mod * math.sin(angle)
    
    vx = vmod * math.cos(angle + math.pi/2)
    vy = vmod * math.sin(angle + math.pi/2)
    return x, y, vx, vy

def pygame_animation(*Bodys):
    screen = pygame.display.set_mode((960, 960), flags=pygame.RESIZABLE)
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption("Gravity simulation!")
    
    scale_coord = max([body.pos.mod() for body in Bodys])*1.1
    
    fps_limit = 600
    run_app = True
    while run_app:
        screen.lock()
        screen.fill(color=(255, 255, 255))
        clock.tick(fps_limit)
        
        calcAccAllObj(*Bodys)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_app = False
        
        for body in Bodys:
            body.display(screen, scale_coord)
                
        pygame.display.flip()
    
    pygame.display.quit()
    pygame.quit()

def test_accuracy(*Bodys : Tuple[Body], interv : int = 1000, iters : int = 1000) -> None:
    errors = [[0 for j in range(iters)] for i in Bodys]
    
    for iter in range(iters):
        for i in range(interv):
            calcAccAllObj(*Bodys)
            
        errs = [(body.pos-Bodys[0].pos).mod() for body in Bodys]
        for i, err in enumerate(errs):        
            errors[i][iter] = err
    
    x = np.arange(0, iters)
    errors = np.array(errors)
    
    maxs = []
    for i, body in enumerate(Bodys):
        max = np.max(errors[i])
        errors[i] /= max
        maxs.append(max)
    
    fig, ax = plt.subplots()
    for i, body in enumerate(Bodys):
        ax.plot(x, errors[i], label=f'{body.name}: {maxs[i]:.3e}')
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()