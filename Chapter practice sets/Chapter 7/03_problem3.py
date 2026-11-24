# 3. Attempt problem 1 using while loop

n = int(input("Enter a number to print its multiplication table : "))

i = 0 
while i<10:
    i += 1
    print(f"\t\t{n} x {i} = {n*i}")