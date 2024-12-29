import random

def cont():
    while True:
        choice = input("Do you want to continue? (yes/no) : ").lower()
        if choice == 'yes':
            start()
        elif choice == 'no':
            print("Thanks for playing the Game!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def start():
    print("Welcome to the game of rock-paper-scissors!")
    user = input("'r'->rock. 'p'->paper. 's'->scissors : ").lower()
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        print("It's a tie")
    elif win(user, computer):
        print("You win")
    else:
        print("You lose")
    
    cont()  # Prompts user if they still want to play or not after displaying results

def win(player, opp):
    if (player == 'r' and opp == 's') or (player == 's' and opp == 'p') or (player == 'p' and opp == 'r'):
        return True

start()