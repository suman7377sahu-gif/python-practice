# 4. Add a static method in problem 2, to greet the user with hello

class Calculator:
    @staticmethod
    def greet():
        print("Hello sir , Welcome to my Calculator program ")
        
    def getSquare(self,n):
        return f" square of {n} is {n**2} "
    def getCube(self,n):
        return f"Cube of {n} is {n**3} "
    def getSqrt(self,n):
        if n < 0:
            return "Square root of negative numbers is not supported."
        return f"Square root of {n} is {int(n**0.5)} "


cal = Calculator()
cal.greet()
num1 = int(input("Enter a to number to get Cube of : "))
print(cal.getCube(num1))
num2 = int(input("Enter a number to get square of : "))
print(cal.getSquare(num2))
num3 = int(input("Enter a number to know the square root of it : "))
print(cal.getSqrt(num3))