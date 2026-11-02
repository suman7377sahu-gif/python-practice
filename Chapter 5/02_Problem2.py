# 2. Write a program to input eight numbers from the user and display all the unique numbers
# (once).
s = set()

E1 = input("Enter number 1: ")
s.add(int(E1))
E2 = input("Enter number 2: ")
s.add(int(E2))
E3 = input("Enter number 3: ")
s.add(int(E3))
E4 = input("Enter number 4: ")
s.add(int(E4))
E5 = input("Enter number 5: ")
s.add(int(E5))
E6 = input("Enter number 6: ")
s.add(int(E6))
E7 = input("Enter number 7: ")
s.add(int(E7))
E8 = input("Enter number 8: ")
s.add(int(E8))

print("The unique numbers are:", s)