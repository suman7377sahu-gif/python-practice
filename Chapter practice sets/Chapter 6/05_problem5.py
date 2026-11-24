# 5. Write a program which finds out whether a given name is present in a list or not.
names = ["Amit", "Ayush", "Chinmaya", "Suman", "Subham"]

name = input("Enter your name :")

if name in names:
    print("The given name is present in the list.")
else:
    print("The given name is not present in the list.")