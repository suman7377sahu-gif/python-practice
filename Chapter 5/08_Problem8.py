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

#in this the value may be remain same for the different key but the key must be the unique otherwise it replace the value of the first key with the value of the second key.