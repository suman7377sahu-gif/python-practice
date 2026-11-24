# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("Chapter 9/log.txt") as f :
    content = f.read()

if ("python" in content):
    print("Yes, python is present in the log file. ")

else :
    print("No, python is not present in the log file. ")
