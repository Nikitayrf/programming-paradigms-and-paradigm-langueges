import math


def main():
    circle_1 = Circle(2)
    print(circle_1.get_area())
    print()
    print(circle_1.get_perimeter())

    triangle = Triangle(3, 4, 5)
    print(triangle.get_area())
    print()
    print(triangle.get_perimeter())


class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        polu_perimetr = self.get_perimeter() / 2
        return math.sqrt(polu_perimetr * (polu_perimetr - self.a)
                         * (polu_perimetr - self.b) * (polu_perimetr - self.c))


if __name__ == '__main__':
    main()
