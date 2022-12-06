'''
Vector Class (5 kyu)
https://www.codewars.com/kata/532a69ee484b0e27120000b6/train/python
'''

class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.x, self.y, self.z = args[0]
        else:
            self.x, self.y, self.z = args

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5