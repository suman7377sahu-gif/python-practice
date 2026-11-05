# import random 

# list = ["s","w","g"]
# computer_choice = random.choice(list)

# print("1. \"s\" for snake .")
# print("2. \"w\" for water .")
# print("3. \"g\" for gun .")
# user_choice = input("Enter Your choice: ")
# if user_choice == "s" or user_choice == "w" or user_choice == "g":
#     while user_choice == "s" :  
#         if(user_choice == "s" and computer_choice == "w"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You Win!!")
#             break
#         elif(user_choice == "s" and computer_choice =="g" ):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You lose !!")
#             break
#         elif(user_choice =="s" and computer_choice =="s"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("Match tie !!")
#             break
        
#     while user_choice == "w" :
#         if(user_choice == "w" and computer_choice == "g"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You Win!!")
#             break
#         elif(user_choice == "w" and computer_choice == "s" ):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You lose !!")
#             break
#         elif(user_choice == "w" and computer_choice == "w"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("Match tie !!")
#             break
        
#     while user_choice == "g" :
#         if(user_choice == "g" and computer_choice == "s"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You Win!!")
#             break
#         elif(user_choice == "g" and computer_choice == "w" ):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("You lose !!")
#             break
#         elif(user_choice == "g" and computer_choice == "g"):
#             print(f"Your choice is {user_choice} and computer choose {computer_choice} so,the result is : ")
#             print("Match tie !!")
#             break
        
        
# else :
#     print("Enter a valid choice!!!")
                



# The above code is written by me without cheat


#This is the optimal solution as above


# import random

# choices = ["s", "w", "g"]

# computer_choice = random.choice(choices)

# print("1. 's' for Snake")
# print("2. 'w' for Water")
# print("3. 'g' for Gun")

# user_choice = input("Enter your choice: ")

# if user_choice not in choices:
#     print("Enter a valid choice!")

# elif user_choice == computer_choice:
#     print("Match tie!")

# elif (user_choice == "s" and computer_choice == "w") or \
#      (user_choice == "w" and computer_choice == "g") or \
#      (user_choice == "g" and computer_choice == "s"):

#     print("You Win!!")

# else:
#     print("You Lose!!")

# print(f"Your choice: {user_choice}")
# print(f"Computer choice: {computer_choice}")




import random # From here i used ChatGPT to know the continuous program logic

choices = ["s", "w", "g"]

user_score = 0
computer_score = 0

print("====== SNAKE WATER GUN GAME ======")

while True:

    computer_choice = random.choice(choices)

    print("\nChoose your option:")
    print("1. 's' for Snake")
    print("2. 'w' for Water")
    print("3. 'g' for Gun")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter s, w or g.")
        continue

    print(f"\nYour choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("Match Tie!")

    elif (user_choice == "s" and computer_choice == "w") or \
         (user_choice == "w" and computer_choice == "g") or \
         (user_choice == "g" and computer_choice == "s"):

        print("You Win!!")
        user_score += 1

    else:
        print("You Lose!!")
        computer_score += 1

    print("\n------ CURRENT SCORE ------")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        break

print("\n====== FINAL RESULT ======")
print(f"Your Final Score: {user_score}")
print(f"Computer Final Score: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game.")

elif user_score < computer_score:
    print("Computer won the game!")

else:
    print("The overall game is a tie!")

print("\nThanks for playing!")