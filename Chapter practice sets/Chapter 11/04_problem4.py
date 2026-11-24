    # 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex :
        def __init__(self, r, i):
            self.r = r #Real part of the complex number
            self.i = i #Imaginary part of the complex number 

        def __add__(self, c2):
            return Complex(self.r + c2.r, self.i + c2.i)

        def __mul__(self,c2):
            real_part = (self.r * c2.r) - (self.i * c2.i)
            imag_part = (self.r * c2.i) + (self.i * c2.r)
            return Complex(real_part , imag_part)

        def __str__(self):
            if self.i < 0:
                return f"{self.r} - {-self.i}i"
            return f"{self.r} + {self.i}i"
c1 = Complex(3,9)
c2 = Complex(1,7)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"Addition (c1 + c2) = {c1 + c2}")       
print(f"Multiplication (c1 * c2) = {c1 * c2}")
