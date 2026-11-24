# 3. A list contains the multiplication table of 7. Write a program to convert it to vertical string
# of same numbers.
# 7
# 14
# .
# .
# .


number = int(input("Enter number to get table of :"))
table =[number*i for i in range(1,11)]
print("\n".join(map(str,table)))