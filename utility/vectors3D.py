from typing import Tuple
import math
import numpy as np
from .vectors2D import Vector2D

# Definition of the class Vector3D
class Vector3D:
    def __init__(self, x : float, y : float, z : float) -> None:
        self.x : float = x
        self.y : float = y
        self.z : float = z
        
    def __str__(self) -> str:
        return f"Coordinate cartesiane \t(x: {self.x:+.2e}, \ty: {self.y:+.2e},\tz: {self.z:+.2e})\n"\
            + f"Coordinate polari      \t(r: {self.mod():+.2e}, \tɸ: {self.azm_angle():+.2e},\tθ: {self.pol_angle():+.2e})\n"\
            + f"Coordinate cilindriche \t(ρ: {self.rho():+.2e}, \tφ: {self.azm_angle():+.2e},\tz: {self.z:+.2e})\n"
            
    def __repr__(self) -> str:
        return f"{self.x} {self.y} {self.z}"
            
    def __eq__(self, other : object) -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __add__(self, other : object) -> object:
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __neg__(self) -> object:
        return Vector3D(-self.x, -self.y, -self.z)
    
    def __sub__(self, other : object) -> object:
        return self + -other
    
    def __mul__(self, other : int|float|object) -> float:
        if isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int|float):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise Exception("Multiplication types unsupported\n")
    
    def __rmul__(self, other : int|float) -> float:#note that in right multiplication self is at the right and other at the left
        if isinstance(other, int|float):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise Exception("Multiplication types unsupported\n")
    
    #NOTE @ è usato come simbolo di prodotto vettoriale (perché è un effettiva moltiplicazione tra matrici)
    def __matmul__(self, other : object) -> object:
        s1 : float = self.y * other.z - self.z * other.y
        s2 : float = self.z * other.x - self.x * other.z
        s3 : float = self.x * other.y - self.y * other.x
        return Vector3D(s1, s2, s3)
    
    def __truediv__(self, other : int|float) -> object:
        if isinstance(other, int|float):
            if other == 0:
                raise Exception("Division by zero!\n")
            return self * (1/other)
        else:
            raise Exception("Division types unsupported\n")
    
    #NOTE la potenza di un vettore + il prodotto scalare con se stesso
    def __pow__(self, other : int) -> float:
        if isinstance(other, int):
            if other > 1:
                return self * self**(other -1)
            elif other == 1:
                return self
            else:
                raise Exception("Power of a vector should be and integer bigger or equal to 1\n")
        else:
            raise Exception("Exponent is and unsupported type\n")
    
    #Return the cartesian position as a tuple
    def get_cart_coord(self) -> Tuple[float]:
        return self.x, self.y, self.z
    
    #Return the polar position as a tuple
    def get_polar_coord(self) -> Tuple[float]:
        return self.mod(), self.azm_angle(), self.pol_angle()
    
    #Return the cylindrical position as a tuple
    def get_cylindrical_coord(self) -> Tuple[float]:
        return Vector2D(self.x, self.y).mod(), self.azm_angle(), self.z
    
    #Modulo
    def mod(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**.5
    
    #Calcola l'angolo azimutale del vettore in coordinate polari
    def azm_angle(self) -> float:
        if self.mod() == 0:
            raise Exception("The vector is a zero: it's not possible to define an Azimuth angle\n")
        if self.x == 0:
            return 0
        theta = math.atan(self.y/self.x)
        if self.x < 0:
            theta += math.pi
        return theta
    
    #Calcola l'angolo polare del vettore in coordinate polari
    def pol_angle(self) -> float:
        if self.mod() == 0:
            raise Exception("The vector is a zero: it's not possible to define a polar angle\n")

        return math.acos(self.z/self.mod())
    
    #Calcola il valore ρ per le coordinate cilindriche
    #NOTE il valore di φ delle coordinate cilindriche è uguale al valore φ delle coordinate polari
    def rho(self) -> float:
        return Vector2D(self.x, self.y).mod()
        
    #Ruota il vettore di un angolo rispetto a x, y, e/o z
    #NOTE la rotazione avviene in senso orario rispetto all'asse (regola mano destra)
    def rotate(self, alpha_x : float = 0, alpha_y : float = 0, alpha_z : float = 0) -> None:
        alpha_x *= -1
        alpha_y *= -1
        alpha_z *= -1
        Rx = np.array([[1, 0 ,0],
              [0, math.cos(alpha_x), -math.sin(alpha_x)],
              [0, math.sin(alpha_x), math.cos(alpha_x)]])
        Ry = np.array([[math.cos(alpha_y), 0, math.sin(alpha_y)],
              [0, 1, 0],
              [-math.sin(alpha_y), 0, math.cos(alpha_y)]])
        Rz = np.array([[math.cos(alpha_z), -math.sin(alpha_z), 0],
              [math.sin(alpha_z), math.cos(alpha_z), 0],
              [0, 0, 1]])
        vec = np.array([self.x, self.y, self.z])
        res = vec @ Rx @ Ry @ Rz
        self.x = res[0]
        self.y = res[1]
        self.z = res[2]