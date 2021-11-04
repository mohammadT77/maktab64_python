from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def __init__(self, *sides):  # Note: This method is NOT abstract! (You may not override it)
        self.sides = sides

    def num_of_side(self):
        return len(self.sides)

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        return sum(self.sides)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.sides}>"

    def __eq__(self, other):
        return set(self.sides) == set(other.sides)


class Triangle(Shape):

    def __init__(self, A, B, C):
        super().__init__(A, B, C)

    @staticmethod
    def heron_formula(s, a, b, c):
        """
        Reference: https://en.wikipedia.org/wiki/Heron's_formula
        :param s: Semi-Perimeter (نصف محیط)
        :param a: Length of side A
        :param b: Length of side B
        :param c: Length of side C
        """
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def area(self):
        return self.heron_formula(self.perimeter() / 2, *self.sides)


class Rectangle(Shape):

    def __init__(self, X, Y):
        super().__init__(X, Y, X, Y)

    def area(self):
        X, Y = self.sides[:2]
        return X * Y


class Square(Rectangle):

    def __init__(self, X):
        super().__init__(X, X)


print("\nTriangle:", t1 := Triangle(5, 4, 3))
print(t1.perimeter())
print(t1.area())
print(t1.num_of_side())
print(Triangle(4, 4, 5) == Triangle(5, 4, 4))

print("\nRectangle:", r1 := Rectangle(10, 5))
print(r1.perimeter())
print(r1.area())
print(r1.num_of_side())
print(Rectangle(4, 4) == Rectangle(3, 4))

print("\nSquare:", s1 := Square(3))
print(s1.perimeter())
print(s1.area())
print(s1.num_of_side())
print(Square(4) == Square(3))
