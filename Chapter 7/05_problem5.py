# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number to find the sum of first natural numbers : "))
i = 1
sum = 0
while i <= n:
    sum += i
    i+=1

print(sum)