import unittest as utest
from triangle import Triangle


# Writing tests...

class TriangleTest(utest.TestCase):

    def setUp(self) -> None:
        self.t1 = Triangle((0, 0), (0, 3), (4, 0))
        self.t2 = Triangle((0, 0), (0, 1), (4, 0))

    def test_area(self):
        self.assertEqual(self.t1.area(), 6)  # assert ... == 6
        self.assertEqual(self.t2.area(), 2)  # assert t2.area() == 2
        # self.assertSetEqual(t1.sides(), (3,5,4))

    def test_sides(self):
        self.assertEqual(set(self.t1.sides()), {5, 4, 3})  # set(t1.sides()) == {5, 3, 4}
        self.assertEqual(set(self.t2.sides()), {1, 4, 17 ** 0.5})  # set(t2.sides()) == {1, 4, 17 ** 0.5}

    def test_perimeter(self):
        self.assertEqual(self.t1.perimeter(), 12)  # t1.perimeter() == 12
        self.assertEqual(self.t2.perimeter(), sum({1, 4, 17 ** 0.5}))  # t2.perimeter() == sum({1, 4, 17 ** 0.5})
