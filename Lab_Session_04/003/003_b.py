# Operating System: Windows 10
# IDE : Microsoft Visual Studio Code 2019
# Python Version : Python 3.10.0

# Last update by RAJENDRA KUJUR(214161008) on 14-09-2021 at 22:01

# This program is a simulation of finite state machine
# where the reading inputs will be characters a-z only
# and prints the final state
# or the number of strings halts at different states
# according to user choices

import random
import os

# simulate the string by using table from file file_name
def simulateString(string, file_name):

    # opens the given file in read mode
    read_file = open(file_name, "r")

    # start from the first node
    current_position = 0
    # store the entire file into paragraph
    paragraph = read_file.read()

    # split paragraph and store each line into line list
    line = paragraph.split("\n")

    # traverse the entire string one by one
    for _ in range(len(string)):

        numbers = line[current_position].split(" ")
        current_position = int(numbers[ord(string[_]) - 97])

    return current_position


# driver code
if os.path.exists("003_b_input.txt"):

    input_file = open("003_b_input.txt", "r")
    table_file = input_file.readline()
    table_file = table_file.strip()

    number_of_string = input_file.readline()
    number_of_string = number_of_string.strip()
    number_of_string = int(number_of_string)

    length_of_string = input_file.readline()
    length_of_string = length_of_string.strip()
    length_of_string = int(length_of_string)

    if os.path.exists(table_file):

        temp_file = open(table_file, "r")

        count_line = 0
        for _ in temp_file:
            count_line += 1
        temp_file.close()

        number_of_states = count_line
        state_appearance = []

        # start every state count as zero
        for _ in range(number_of_states):
            state_appearance.append(0)

        for number in range(number_of_string):
            string = ""
            # generate a random string of the given length
            for _ in range(length_of_string):
                string += chr(97 + random.randint(0, 25))

            # for each string ending at a state increment its value by 1
            state_appearance[simulateString(string, table_file)] += 1

        # print("\nFinally number of strings halt at states : ")
        # print(state_appearance)

        for _ in range(0, len(state_appearance)):
            state_appearance[_] = state_appearance[_] / number_of_string

        write_file = open("003_b_output.txt", "w")
        if os.path.exists("003_b_output.txt"):
            for index in range(0, len(state_appearance)):
                write_file.write(f"{index+1} : {state_appearance[index]}\n")
            write_file.close()
        else:
            print("Unable to open output file.")
    else:
        print("Unable to find transition table input file.")
    input_file.close()
else:
    print("Can't find the input files.")
