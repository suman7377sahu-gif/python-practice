# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Demo :
    a = 10
    def __init__(self):
        pass

obj = Demo()
print(obj.a)

obj.a = 0
print(obj.a)#instance attribute 
print(Demo.a)# class attribute
# by obj.a = 0 doesn't change the class attribute it only assign the value of instance attribute
