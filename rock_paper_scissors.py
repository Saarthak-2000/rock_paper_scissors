import random
# Get user input
user_input = input("Enter 'rock', 'paper', or 'scissors': ")

# Convert user input to lowercase for case-insensitive comparison
user_input = user_input.lower()

# Define the possible choices
choices = ['rock', 'paper', 'scissors']

# Check if the user input is valid
if user_input in choices:
    # Generate a random choice for the computer
    computer_choice = choices[random.randint(0, 2)]

    # Print the user and computer choices
    print("You chose:", user_input)
    print("Computer chose:", computer_choice)

    # Determine the winner
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose.")
else:
    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")