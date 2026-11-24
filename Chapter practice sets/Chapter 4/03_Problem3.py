# 3. Check that a tuple type cannot be changed in python.
t = (1, 2, 3, 4, 5)
print(t)
# t[0] = 10   This will raise an error as tuples are immutable
print(t)
