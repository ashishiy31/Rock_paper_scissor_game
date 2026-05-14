import random

# 1. Setup the list
item_list = ["rock", "paper", "scissor"]

# 2. Get user input and force it to lowercase
user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()

# 3. Pick the computer choice ONCE
comp_choice = random.choice(item_list)

# 4. Display what the computer chose
print(f"Computer chose: {comp_choice}")

# 5. Result Logic
if user_choice not in item_list:
    print("Invalid input! Please check your spelling.")
elif user_choice == comp_choice:
    print("It's a tie!")
elif (user_choice == "rock" and comp_choice == "scissor") or \
     (user_choice == "paper" and comp_choice == "rock") or \
     (user_choice == "scissor" and comp_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")

print("Thank you for playing!")