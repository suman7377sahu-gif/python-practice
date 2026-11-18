# 5. Write a class vector representing a vector of 3 dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)

    def __mul__(self, v2):
        return (self.x * v2.x) + (self.y * v2.y) + (self.z * v2.z)

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"


v1 = Vector(1, 4, 6)
v2 = Vector(2, 3, 5)

print("Sum:", v1 + v2)          
print("Dot Product:", v1 * v2)  