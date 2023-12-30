from typing import Tuple
import math
import warnings

# Definition of the class Vector2d
class Vector2D:
    def __init__(self, x : float, y : float) -> None:
        self.x : float = x
        self.y : float = y
        
    def __str__(self) -> str:
        return f"Coordinate cartesiane \t(x: {self.x:+.2e},\ty: {self.y:+.2e})\n"\
            + f"Coordinate polari      \t(r: {self.mod():+.2e},\tɸ: {self.angle():+.2e})\n"
            
    def __repr__(self) -> str:
        return f"{self.x} {self.y}"
            
    def __eq__(self, other : object) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other : object) -> object:
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __neg__(self) -> object:
        return Vector2D(-self.x, -self.y)
    
    def __sub__(self, other : object) -> object:
        return self + -other
    
    def __mul__(self, other : int|float|object) -> float:
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int|float):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise Exception("Multiplication types unsupported\n")
    
    def __rmul__(self, other : int|float) -> float:
        if isinstance(other, int|float):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise Exception("Multiplication types unsupported\n")
    
    #NOTE matmul @ è usato come simbolo di prodotto vettoriale non come prodotto di matrici
    #NOTE in 2D crea in warning perché non si può definire un vettore in una terza dimensione perché non esiste, return il modulo di tale vettore
    def __matmul__(self, other : object) -> float:
        warnings.warn("Warning: you are tring to get the vector product in 2D, since it's defined only in 3D the module of the vector was returned insted of the vector.\n")
        return self.x*other.y - other.x*self.y
    
    def __truediv__(self, other : int|float) -> object:
        if isinstance(other, int|float):
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
        return self.x, self.y
    
    #Return the polar position as a tuple
    def get_polr_coord(self) -> Tuple[float]:
        return self.mod(), self.angle()
    
    #Modulo
    def mod(self) -> float:
        return (self.x**2 + self.y**2)**.5
    
    #Calcola l'angolo polare del vettore
    def angle(self) -> float:
        if self.mod() == 0:
            raise Exception("The vector is a zero: it's not possible to define a polar angle\n")
        if self.x == 0:
            return 0
        theta = math.atan(self.y/self.x)
        if self.x < 0:
            theta += math.pi
        return theta
    
    #Ruota il vettore
    def rotate(self, theta : float) -> None:
        mod = self.mod()
        alpha = self.angle()
        self.x = mod * math.cos(alpha + theta)
        self.y = mod * math.sin(alpha + theta)