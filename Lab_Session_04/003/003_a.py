# Operating System: Windows 10
# IDE : Microsoft Visual Studio Code 2019
# Python Version : Python 3.10.0


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

    string = string.lower()
    # traverse the entire string one by one
    for _ in range(len(string)):

        numbers = line[current_position].split(" ")
        current_position = int(numbers[ord(string[_]) - 97])

    return current_position


if os.path.exists("003_input.txt"):

    input_file = open("003_input.txt", "r")

    table_file = input_file.readline()
    table_file = table_file.strip()

    string_file = input_file.readline()
    string_file = string_file.strip()

    if os.path.exists(table_file):

        if os.path.exists(string_file):

            read_string = open(string_file, "r")
            string = read_string.readline().strip()
            read_string.close()

            # simulate the string to the given table in file read_table
            write_file = open("003_a_output.txt", "w")

            if os.path.exists("003_a_output.txt"):
                write_file.writelines(
                    f"Ending at state : {simulateString(string, table_file)}"
                )
            else:
                print("Unable to create output File.")
        else:
            print("Can't find the string input file.")
    else:
        print("Unable to find transition table input file.")
    input_file.close()
else:
    print("Can't find the input files.")
