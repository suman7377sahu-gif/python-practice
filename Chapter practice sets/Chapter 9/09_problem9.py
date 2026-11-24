# 9. Write a program to find out whether a file is identical and matches the content of another
# file.

with open("Chapter 9/This.txt") as f :
    content1 = f.read()

with open("Chapter 9/This_copy.txt") as f :
    content2 = f.read()


if content1 == content2 :
    print("Both files are identical in manner.")

else :
    print("Both files are not identical in manner.")