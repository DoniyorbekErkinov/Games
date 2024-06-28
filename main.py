import random

# If game ends ask if user wants continue or not
def continue_or_not(game_func): 
        answer = input("Do you want to continue? (Yes/No)\n").strip().lower()
    
        if answer in ("yes", "y", "ye"):
            game_func()
        elif answer in ("no", "n"):
            print("Game ended.")
        else:
            print("Wrong input")
            game_func()
            
# Function to play the number guessing game
def first_game():
    chosen_number = int(input("Choose a number between 1 and 10\n"))
    bot_chosen_number = random.randint(1, 10)
    
    if chosen_number == bot_chosen_number:
        print("Player won!!!")
        continue_or_not(first_game())
    else:
        print(f"Player lost! The bot chose {bot_chosen_number}")
        continue_or_not(first_game())

# Function to play the rock scissor paper game
def second_game():    
    chosen_number = int(input("Choose a number between 1 and 3\n 1: Rock 2: Scissor 3: Paper\n"))
    bot_chosen_number = random.randint(1, 3)
    if chosen_number == 1 and bot_chosen_number == 2:
        print("Player won! Bot chose Scissor")
        continue_or_not(second_game)
    elif chosen_number == 1 and bot_chosen_number == 3:
        print("Player lost! Bot chose Paper")
        continue_or_not(second_game)
    elif chosen_number == 2 and bot_chosen_number == 1:
        print("Player lost! Bot chose Rock")
        continue_or_not(second_game)
    elif chosen_number == 2 and bot_chosen_number == 3:
        print("Player won! Bot chose Paper")
        continue_or_not(second_game)
    elif chosen_number == 3 and bot_chosen_number == 1:
        print("Player won! Bot chose Rock")
        continue_or_not(second_game)
    elif chosen_number == 3 and bot_chosen_number == 2:
        print("Player lost! Bot chose Scissor")
        continue_or_not(second_game)
    else:
        print("Wrong input!")
        continue_or_not(second_game)        
    

# Function to start the game
def start_game():
    answer = input("Do you want to start the game? (Yes/No)\n").strip().lower()
    
    if answer in ("yes", "y", "ye"):
        print("Your answer should be a number")
        game_choice = int(input("Which game do you want to play?\nGames:\n1. Guess a number\n2. Rock Scissor and Paper\n"))
        
        if game_choice == 1:
            first_game()
        elif game_choice == 2:
            second_game()
        else:
            print("Invalid game choice. Starting over.")
            start_game()
        
    elif answer in ("no", "n"):
        print("Game ended.")
    else:
        print("Wrong input")
        start_game()

# Start the game
start_game()
