# 4. Write a program to find whether a given username contains less than 10 characters or not.
name = input("Enter your username :")

if len(name) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username does not contain less than 10 characters.")