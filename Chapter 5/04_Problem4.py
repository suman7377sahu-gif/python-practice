# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s)) # The length of the set s will be 2, because 20 (int) and 20.0 (float) are considered equal in Python, so only one of them will be stored in the set. The string '20' is a different type, so it will be stored as a separate value.

#we can also write as s.update([20, 20.0, '20']) # this will also add the same values to the set s, and the length will still be 2. beacause 20 (int) and 20.0 (float) are considered equal in Python, so only one of them will be stored in the set. The string '20' is a different type, so it will be stored as a separate value.