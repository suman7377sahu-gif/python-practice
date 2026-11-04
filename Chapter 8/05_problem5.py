# 5. Write a python function to print first n lines of the following pattern.
# ***
# ** - for n = 3
# *
def pattern1(rows):
    for i in range(rows,0,-1):
        print("*"*i,end="")
        print()

row_numbers = int(input("Enter number of Rows: "))
pattern1(row_numbers)