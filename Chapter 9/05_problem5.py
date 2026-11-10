# 5. Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "gali", "chor","ganda"]

with open("Chapter 9/Donkey.txt") as f :
    content = f.read()

    for word in words :
        content = content.replace(word,"#" * len(word))

with open("Chapter 9/Donkey.txt","w") as f :
    f.write(content)

print("censored Content is updated ")
