# 6. Write __str__() method to print the vector as follows: 7i + 8j + 10k
class Vector:
    def __init__(self, l):
        self.l = l

    def __str__(self):
        return f"{self.l[0]}i + {self.l[1]}j + {self.l[2]}k"


v = Vector([7, 8, 10])
print(v)  