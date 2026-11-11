# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:

    def getSquare(self,n):
        return n**2
    def getCube(self,n):
        return n**3
    def getSqrt(self,n):
        if n < 0:
            return "Square root of negative numbers is not supported."
        return n**0.5


cal = Calculator()

print(cal.getCube(2))
print(cal.getSquare(5))
print(int(cal.getSqrt(25)))