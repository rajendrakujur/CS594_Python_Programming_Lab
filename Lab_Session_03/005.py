# This program is last updated by RAJENDRA KUJUR (214161008) on 27-08-2021 at 17:23

# import module for random number generation
import random


# function to play Player vs Computer
def playAgainstComputer(number, limit):

    while True:
        system_generated = random.randint(1, limit)
        print(f"Computer generated : {system_generated}")
        number -= system_generated

        if number <= 0:
            print("Computer won.")
            break

        user_number = int(input(f"Enter your number (1-{limit}): "))

        # if number entered is outside the limit then prompt to enter valid number
        while user_number > limit or user_number < 1:
            print(f'Print number between 1 to {limit} :')
            user_number = int(input())

        number -= user_number

        if number <= 0:
            print("You won.")
            break


# function to play Computer vs Computer
def computerVsComputer(number, limit):

    while True:
        system_generated = random.randint(1, limit)
        print(f"Computer_1 generated : {system_generated}")
        number -= system_generated

        if number <= 0:
            print("Computer_1 won.")
            break

        system_generated = random.randint(1, limit)
        print(f"Computer_2 generated : {system_generated}")
        number -= system_generated

        if number <= 0:
            print("Computer_2 won.")
            break


# Function to play Player Vs Player
def playerVsPlayer(number, limit):

    while True:
        user_1_number = int(input(f"Player_1 turn (1-{limit}): "))

        # if number entered is outside the limit then prompt to enter valid number
        while user_1_number > limit or user_1_number < 1:
            print(f'Print number between 1 to {limit} :')
            user_1_number = int(input())

        number -= user_1_number

        if number <= 0:
            print("Player_1 won.")
            break

        user_2_number = int(input(f"Player_2 turn (1-{limit}): "))

        # if number entered is outside the limit then prompt to enter valid number
        while user_2_number > limit or user_2_number < 1:
            print(f'Print number between 1 to {limit} :')
            user_2_number = int(input())

        number -= user_2_number

        if number <= 0:
            print("Player_2 won.")
            break


# function to play game
def playMarblesGame(total_numbers, skip_numbers):

    # making a list to store numbers from 1 to N
    input_list = []
    for index in range(total_numbers):
        input_list.append(index + 1)

    # starting index will be zero
    current_index = 0
    # list to store the removing element's sequence
    output_list = []

    while len(input_list):
        removing_index = (current_index + skip_numbers - 1) % len(input_list)
        output_list.append(input_list[removing_index])
        del input_list[removing_index]
        current_index = removing_index

    print('Sequence of getting out the marbles is :')
    print(output_list)
    print(f'Last element to get out : {output_list[len(output_list)-1]}')


# execution begins here
while True:
    n = int(input("Enter n : "))
    k = int(input("Enter k : "))

    # ask user choice which game s/he wants to play
    print('Which game you want to play?')
    print('(1) Removing Marbles from a circular list')
    print('(2) Removing number from a linear list')
    game_choice = int(input())

    if game_choice == 1:
        playMarblesGame(n, k)

    elif game_choice == 2:
        while True:
            # if user selects 2nd option choose available modes
            print('Select Modes :')
            print('(1) For Computer vs Player')
            print('(2) For Computer_1 vs Computer_2')
            print('(3) For Player_1 vs Player_2')

            choice = int(input())

            if choice == 1:
                playAgainstComputer(n, k)
                break
            elif choice == 2:
                computerVsComputer(n, k)
                break
            elif choice == 3:
                playerVsPlayer(n, k)
                break
            else:
                # If user gives input some other number as choice
                print('Enter valid chioice.')
                continue
    # if user gives invalid chice
    else:
        print('Enter valid chioice.')
        continue

    # prompt the user if wants to play again
    if input("Play next game? yes or no?\n").lower() == 'yes':
        continue
    else:
        break
