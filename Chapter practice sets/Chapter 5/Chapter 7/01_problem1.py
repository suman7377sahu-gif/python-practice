# 1. Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter a number to print its multiplication table: "))


print(f"---Multiplication table of {n} ---")


for i in range(1,11):
    print(f"\t\t{n} x {i} = {n*i}")

