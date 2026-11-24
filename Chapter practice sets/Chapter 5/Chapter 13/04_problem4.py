# 4. Write a program to filter a list of numbers which are divisible by 5.
def Divby5(l):
     if (l%5 == 0 ):
        return True 
     return False
     
l1 = [5,25,67,90,78,45,65,33,44,55]

filtered_list = list(filter(Divby5,l1))

print(filtered_list)


