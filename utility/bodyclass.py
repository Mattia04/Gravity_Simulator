from typing import Tuple
from os import path

import json

from .vectors2D import Vector2D

with open(path.abspath("Settings.json"), "r") as f:
    config = json.load(f)
dt = config["dt"]


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
 
    #Return all available information, Cart = cartesian mode, Polar = polar mode
    def __str__(self, mode = "Short"):
        return f"Il corpo {self.name}\n"\
            + f"Si trova nelle coordinate cartesiane ({self.pos.x:.3g}m, {self.pos.y:.3g}m).\n"\
            + f"Si muove con velocità cartesiane     ({self.vel.x:.3g}m/s, {self.vel.y:.3g}m/s).\n"\
            + f"Con accelerazione di                 ({self.acc.x:.3g}m/s^2, {self.acc.y:.3g}m/s^2)"
        
    #Return all available information in a str[tuple]
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
    
    #Set the acceleration from external input
    def setAcceleration(self, other : Vector2D) -> None:
        self.acc = other
        self.accelerate()
        self.move()