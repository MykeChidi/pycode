import random
from colorama import Fore

player = 0
computer = 0

player_choices = {'1':'rock', '2':'paper', '3':'scissors'}
computer_choices = ['rock', 'paper', 'scissors']

print(Fore.BLUE,"\n\t__ROCK PAPER SCISSORS GAME__\n")
print("Enter 'q' to quit")
print("Enter '1' to choose rock.\nEnter '2' to choose paper \nEnter '3' to choose scissors")

while True:
    player_choice = input("\nEnter a choice (1, 2, 3): ").lower()
    if player_choice =='q':
        print(Fore.YELLOW, "\n\tThanks for playing!\n\t_Final Scores_")
        print("\n\tPlayer final score:", player)
        print("\tComputer final score:", computer)
        if player < computer:
            print("\n\t**Computer Wins This Round!**💎🥇\n")
        elif player > computer:
            print("\n\t**Player Wins This Round!**💎🥇\n")
        else:
            print("\n\tIt's a Tie!")
        break
    
    if player_choice not in player_choices:
        print(Fore.RED, "\nPls Enter 1, 2, 3 or 'q' to quit")
        continue

    computer_choice = random.choice(computer_choices)
    try:
        player_choice = player_choices[player_choice]
    except KeyError:
        pass

    print(Fore.GREEN, "You chose:", player_choice)
    print(Fore.GREEN, "Computer`s choice:" , computer_choice)

    if player_choice == computer_choice:
        print("Draw No Scores")
    elif ((player_choice == 'rock' and computer_choice == 'scissors') 
          or (player_choice == 'paper' and computer_choice == 'rock') 
          or (player_choice == 'scissors' and computer_choice == 'paper')):
        print("Player won")
        player += 1
    else:
        print("Computer won")
        computer += 1
