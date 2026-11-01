# Label the program written in problem 4 with comments.
# Write a python program to print the contents of a directory using the os module. Search
#  online for the function which does that.
import os 

# Specify the path of the directory you want to list
path = './'

# Use os.listdir() to get a list of all items in the directory
items = os.listdir(path)

print(items)