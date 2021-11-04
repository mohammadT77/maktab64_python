class Triangle:
    A: tuple
    B: tuple
    C: tuple

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def area(self):
        return self.heron_formula(self.A, self.B, self.C)

    def sides(self):
        return self.distance(self.A, self.B), \
               self.distance(self.A, self.C), \
               self.distance(self.C, self.B)

    def perimeter(self):
        return sum(self.sides())

    @staticmethod
    def heron_formula(A, B, C) -> int:
        return 0.5 * abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

    @staticmethod
    def distance(A, B):
        return ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5


t1 = Triangle((0, 0), (0, 3), (4, 0))
print(t1.area())
print(t1.sides())
print(t1.perimeter())
