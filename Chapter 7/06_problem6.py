# 6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter a number to get the factorial : "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")