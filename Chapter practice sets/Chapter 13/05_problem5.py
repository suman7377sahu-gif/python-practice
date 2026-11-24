# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
def Max(a,b):
    if a>b :
        return a
    return b
l1 = [1,2,3,4,5,6,7,8,9,0]

maximum_number = reduce(Max,l1)
print(maximum_number)