import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'rock' and computer_choice == 'water') or \
       (user_choice == 'paper' and computer_choice == 'water') or \
       (user_choice == 'scissors' and computer_choice == 'water'):
        return "You win!"

    return "You lose."

def main():
    print("Enter your choice = rock, paper, scissors, or water")
    user_choice = input().lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors', 'water'])

    print("Computer chose", computer_choice)
    print("User Choice = ",user_choice)
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()