# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt .
number = int(input("Enter a number to get multiplication table: "))
table = [f"{number} X {i} = {number*i}" for i in range(1,11) ]

with open("Chapter 12/tables.txt","w") as f:
    f.write("\n".join(table))
print(table)