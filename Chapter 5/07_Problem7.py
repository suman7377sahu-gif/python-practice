# 7. If the names of 2 friends are same; what will happen to the program in problem 6?


d = {}
n1 = input("Enter your name :")
l1=  input("Enter your favorite language :")
d.update({n1:l1})
n2 = input("Enter your name :")
l2= input("Enter your favorite language :")  
d.update({n2:l2})
n3 = input("Enter your name :")
l3= input("Enter your favorite language :")
d.update({n3:l3})
n4 = input("Enter your name :")
l4= input("Enter your favorite language :")
d.update({n4:l4})
print (f"The dictionary of friends and their favorite languages is:{d}")


#if my two friends have the same name, then the value of the first friend will be replaced by the value of the second friend in the dictionary. This is because dictionaries do not allow duplicate keys, and when a new key-value pair is added with an existing key, it will overwrite the previous value associated with that key.