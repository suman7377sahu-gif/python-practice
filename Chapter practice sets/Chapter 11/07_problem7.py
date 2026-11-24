# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l

    def __add__(self, v2):
        result = [self.l[i] + v2.l[i] for i in range(len(self.l))]
        return Vector(result)

    def __mul__(self, v2):
        return sum(self.l[i] * v2.l[i] for i in range(len(self.l)))

    def __str__(self):
        return f"{self.l[0]}i + {self.l[1]}j + {self.l[2]}k"

    def __len__(self):
        return len(self.l)


v1 = Vector([1, 4, 6])
print(len(v1))  