import random

while True:
    user_input = input("Enter a choice (rock, paper, scissors): ")
    possible_option = ["rock", "paper", "scissors"]
    computer_option = random.choice(possible_option)
    
    if user_input not in possible_option:
        print("Error! Invalid input, try another option")
    if user_input == computer_option:
        print('Both players selected', str(user_input),". It's a tie!","(",user_input,"):(",computer_option,")")
        
    elif user_input == "rock":
        if computer_option == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input == "paper":
        if computer_option == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_input == "scissors":
        if computer_option == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
