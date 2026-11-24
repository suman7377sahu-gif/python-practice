# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "namaste": "hello",
    "dhanyavaad": "thank you",
    "haal": "situation",
    "chabbi": "key",
    "dost": "friend",


}

word = input("Enter a Hindi word to look up its English translation: ")
print(f"The English of your word is :{ words[word]}")