# 4. A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.
with open("Chapter 9/Donkey.txt") as f :

    content = f.read()

content = content.replace("Donkey","#####")

with open("Chapter 9/Donkey.txt","w") as f :
    f.write(content)

print("Donkey word replaced by #####")