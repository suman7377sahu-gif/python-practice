# 8. Write a python function to print multiplication table of a given number.
def table_of_number(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

num= input("Enter your number to print the table:")

table_of_number(int(num))