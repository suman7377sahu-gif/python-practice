# 1. Write a program using functions to find greatest of three numbers
def greatest_among_three(n1,n2,n3):
    if (n1>n2 and n1>n3):
        print(f"{n1} is the greatest among three.")
    elif (n2>n3 and n2>n1):
        print(f"{n2} is the greatest among three.")
    else :
        print(f"{n3} is the greatest among three.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

greatest_among_three(num1,num2,num3)