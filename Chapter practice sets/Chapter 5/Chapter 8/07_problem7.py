# 7. Write a python function to remove a given word from a list and strip it at the same time.
def clean_and_strip(word_list,target_word):
    cleaned_target = target_word.strip()

    result = []

    for word in word_list:
        cleaned_word = word.strip()
        if cleaned_target != cleaned_word:
            result.append(cleaned_word)

    return result



item_list = input("Enter your item list here separating by commas: ")

# item_list.split(",")

word_to_remove = input("Enter the word that you want to remove from list: ")

print(clean_and_strip(item_list.split(","),word_to_remove))