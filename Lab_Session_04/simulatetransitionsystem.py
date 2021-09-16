# Last update by RAJENDRA KUJUR(214161008) on 14-09-2021 at 22:01

# This program is a simulation of finite state machine
# where the reading inputs will be characters a-z only
# and prints the final state
# or the number of strings halts at different states
# according to user choices

import random


# simulate the string by using table from file file_name
def simulateString(string, file_name):

    # opens the given file in read mode
    read_file = open(file_name, 'r')

    # start from the first node
    current_position = 0
    # store the entire file into paragraph
    paragraph = read_file.read()

    # split paragraph and store each line into line list
    line = paragraph.split('\n')

    # traverse the entire string one by one
    for _ in range(len(string)):

        numbers = line[current_position].split(' ')
        current_position = int(numbers[ord(string[_])-97])

    return current_position


# generates table randomly
def tableGenerator(number_of_states):

    # opens/create a new file in write mode
    output_file = open('table.txt', 'w')

    # generate number_of_states lines
    for _ in range(number_of_states):
        line = ''

        # generates number randomly from 1-number_of_states for 26 characters
        for rand_char in range(1, 27):
            line += str(random.randint(0, number_of_states-1))
            line += ' '

        line += '\n'
        output_file.writelines(line)

    output_file.close()


# main function execution begins here
# prompt if user want to give table in form of file or wants table to be generated autmatically
if input('Do you want the program to generate transition table randomly (yes/no)? : ').lower() == 'yes':
    number_of_states = int(
        input('Enter number of states finite Machine should have : '))
    tableGenerator(number_of_states)
    print('Trasition table generated and saved at "table.txt"')
    file_name = 'table.txt'

else:
    file_name = input(
        'Enter file_name from where the transition table has to be read : ')

while True:
    # show menu to the user
    print('\n1.Check the final state')
    print('2.Check the number of string halt at different states')

    choice = int(input('Enter choice : '))
    if choice == 1:

        # prompts if user want to enter string or string to be generated automatically
        if input('Do you want to generate string randomly (yes/no) ? :').lower() == 'yes':

            # ask the user for input string length
            length = int(input('Enter length of string : '))
            string = ''

            # generate a random string of the given length
            for _ in range(length):
                string += chr(97+random.randint(0, 25))

            print(f'\nGenerated String : {string}')

        else:
            string = input('Enter string (a-z characters only): ')

        # simulate the string to the given table in file file_name
        print(f'Ending at state : {simulateString(string, file_name)}')

    elif choice == 2:

        length = int(
            input('Enter length of string that is to be generated : '))
        number_of_strings = int(
            input('Enter number of strings you want to generate : '))

        # make an empty list to store the number of string that ended at particular state
        state_appearance = []

        # start every state count as zero
        for _ in range(number_of_states):
            state_appearance.append(0)

        # generate given number_of_string
        for number in range(number_of_strings):
            string = ''
            # generate a random string of the given length
            for _ in range(length):
                string += chr(97+random.randint(0, 25))

            # for each string ending at a state increment its value by 1
            state_appearance[simulateString(string, file_name)] += 1

        print('\nFinally number of strings halt at states : ')
        print(state_appearance)

    else:
        print('Enter valid choice.')

    # prompt user if wants to continue
    choice = input('Do you want to continue (yes/any other) ? :')

    if choice.lower() == 'yes':
        continue
    else:
        break
