# ''' n = int(input("Enter a number: "))

# # for i in range(1,n+1):
# #     for j in range (1,(2*i-1)+1):
# #         while (n-i):
# #             print(" ",end="")
# #             i+=1
# #         print("*",end="")
# #     print()
# '''


# # the efficient way to print the pattern is as follows:

# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     for j in range (1,n-i+1):
#         print(" ",end="")

#     for k in range (1, (2*i-1)+1):
#         print("*",end="")  

#     print()


n = int(input("Enter a number: "))

for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*" * (2*i-1), end="")
    print()
    