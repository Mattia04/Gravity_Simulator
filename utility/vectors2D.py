from typing import Tuple
import math
import warnings

class Vector2D:
    """__Vector2D__
    ---------
    Contains:
        x: x coordinate of the cartesian plane
        y: y coordinate of the cartesian plane
    ---------
    Raises:
        Warning: When you try to get the vector product of two 2D vectors
            you can't have a vector result in the same plane, so the module of
            the resultant vector is return instead of the actual vector
        Exception: Multiplication types unsupported raises when trying to
            get the product of a vector times an unsupported type.
        Exception: Division types unsupported raises when trying to
            divide a vector by an unsupported type (float|int are the only
            supported types).
        Exception: Exponent is and unsupported type raises when trying to get
            the power of a vector to a non-integer number
        Exception: Power of a vector should be and integer bigger or equal to 1
            raises when trying to get the power of a vector to an integer equal
            or less than 0.
        Exception: The vector is a zero raises when trying to get the polar
            angle of a (0, 0) vector, it's not defined
    """
    def __init__(self, x : float, y : float) -> None:
        self.x : float = x
        self.y : float = y

    def __str__(self) -> str:
        return f"Cartesian coordinates \t(x: {self.x:+.2e},\ty: {self.y:+.2e})\n"\
            +  f"Polar coordinates     \t(r: {self.mod():+.2e},\tɸ: {self.angle():+.2e})\n"

    def __repr__(self) -> str:
        return f"{self.x} {self.y}"

    def __eq__(self, other : object) -> bool:
        """Args:
            other (object): another Vector2D
        --------
        Returns:
            bool: true if other vector is the same as self vector
        """
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __add__(self, other : object) -> object:
        """Definition of additions of vectors
        -----
        Args:
            other (object): another Vector2d
        --------
        Returns:
            object: the sum of self and other as a Vector2D
        """
        return Vector2D(self.x + other.x, self.y + other.y)

    def __neg__(self) -> object:
        """Definition of the negative of a vector
        --------
        Returns:
            object: the opposite of the self vector
        """
        return Vector2D(-self.x, -self.y)

    def __sub__(self, other : object) -> object:
        """Definition of subtraction of vectors
        -----
        Args:
            other (object): another Vector2d
        --------
        Returns:
            object: the difference of self and other as a Vector2D
        """
        return self + -other

    def __mul__(self, other : int|float|object) -> float|object:
        """Definition of right multiplications self * other
        -----
        Args:
            other (object): another Vector2d
            other (int|float): number value
        -------
        Raises:
            Exception: Multiplication types unsupported if other is not
                int|float|object
        --------
        Returns:
            if other is int|float:
                object: the product of a vector times a scalar
            if other is object:
                float: the scalar product of the vectors self and other
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int|float):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise Exception("Multiplication types unsupported\n")

    def __rmul__(self, other : int|float) -> object:
        """Definition of the right multiplication other * self
        -----
        Args:
            other (int | float): number value
        -------
        Raises:
            Exception: Multiplication types unsupported if other is not
                int|float
        --------
        Returns:
            object: the product of a scalar times a vector
        """
        if isinstance(other, int|float):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise Exception("Multiplication types unsupported\n")

    def __matmul__(self, other : object) -> float:
        """Definition of the vector product (self @ other), ! always generates a warning
        -----
        Args:
            other (object): another Vector2D
        -------
        Raises:
            Warning: Since the vector product it's not defined in 2D raises a warning
        --------
        Returns:
            float: the module of the resultant vector
        """
        warnings.warn("Warning: you are trying to get the vector product in 2D, "\
            +"since it's defined only in 3D the module of the vector was "\
            +"returned instead of the vector.\n")
        return self.x*other.y - other.x*self.y

    def __truediv__(self, other : int|float) -> object:
        """Definition of right division self / other
        -----
        Args:
            other (int|float): number value
        -------
        Raises:
            Exception: Division types unsupported if other is not int|float
        --------
        Returns:
            object: the product of a vector times a scalar^(-1)
        """
        if isinstance(other, int|float):
            return self * (1/other)
        else:
            raise Exception("Division types unsupported\n")

    def __pow__(self, other : int) -> float|object:
        """Definition of the power of a vector, self**other
        -----
        Args:
            other (int): the exponent
        -------
        Raises:
            Exception: Power of a vector should be and integer bigger or equal
                to 1, when other <= 0, since it's not defined
            Exception: Exponent is and unsupported type, when other is not int
                since it's not defined
        --------
        Returns:
            The scalar product of self*self other-times, it's type:
                float: if other is even
                object: if other is odd
        """
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
    def get_polar_coord(self) -> Tuple[float]:
        return self.mod(), self.angle()

    #Return the modulus of the vector
    def mod(self) -> float:
        return (self.x**2 + self.y**2)**.5

    #Return the polar angle of the vector
    def angle(self) -> float:
        if self.mod() == 0:
            raise Exception("The vector is a zero\n")
        if self.x == 0:
            return 0
        theta = math.atan(self.y/self.x)
        if self.x < 0:
            theta += math.pi
        return theta

    #Rotate the vector
    def rotate(self, theta : float) -> None:
        mod = self.mod()
        alpha = self.angle()
        self.x = mod * math.cos(alpha + theta)
        self.y = mod * math.sin(alpha + theta)


def Vec2D_from_polar(module : float, theta : float) -> Vector2D:
    return Vector2D(module * math.cos(theta), module * math.sin(theta))
