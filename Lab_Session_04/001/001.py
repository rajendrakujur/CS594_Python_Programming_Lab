# Operating System: Windows 10
# IDE : Microsoft Visual Studio Code 2019
# Python Version : Python 3.10.0

import os

# (a) Read the name of a file, open it and print  the first n lines.
#  (n is a user input integer)
def readFirstNLines():

    if os.path.exists("001_a_input.txt"):

        read_file = open("001_a_input.txt", "r")
        file_name = read_file.readline()
        read_file.close()

        n = int(input("Enter n : "))
        while n < 0:
            n = int(input("Enter valid n : "))
        if os.path.exists(file_name):
            read_file = open(file_name, "r", encoding="utf8")

            write_file = open("001_a_output.txt", "w")
            if os.path.exists("001_a_output.txt"):
                for _ in range(1, n + 1):
                    line = read_file.readline()
                    write_file.writelines(line)
                write_file.close()
            else:
                print("Unable to open output file.")
        else:
            print("File not found.")
    else:
        print("Unable to open input file")


# (b) Read the name of a file, open it and print  the last n lines.
#    (n is a user input integer)
def readLastNLines():

    if os.path.exists("001_b_input.txt"):

        read_file = open("001_b_input.txt", "r")
        file_name = read_file.readline()
        read_file.close()

        n = int(input("Enter n : "))
        while n < 0:
            n = int(input("Enter valid n : "))

        if os.path.exists(file_name):
            read_file = open(file_name, "r", encoding="utf8")

            write_file = open("001_b_output.txt", "w")
            if os.path.exists("001_b_output.txt"):
                for line in read_file.readlines()[-n:]:
                    write_file.writelines(line)
                write_file.close()
            else:
                print("Unable to open output file.")
        else:
            print("File not found.")
    else:
        print("Unable to open input file")


# (c) Read a string x,  file name y and an integer n. Append n copies of x to
#     the file y.
def appendAtLast():

    if os.path.exists("001_c_input.txt"):

        read_file = open("001_c_input.txt", "r")
        str = read_file.readline()
        file_name = read_file.readline()
        file_name = file_name.rstrip()
        n = int(read_file.readline())
        read_file.close()

        if n < 0:
            print("Invalid n value, can't proceed further.")
        else:
            if os.path.exists(file_name):
                append_file = open(file_name, "a")
                for _ in range(1, n + 1):
                    append_file.write(str)
                append_file.close()
            else:
                print("File not found.")
    else:
        print("Unable to open input file")


# (d) Read a string x, file name y and an integer n. Insert  n copies of x  at the beginnning of the file y.
def appendAtBegin():

    if os.path.exists("001_d_input.txt"):

        read_file = open("001_d_input.txt", "r")
        str = read_file.readline()
        file_name = read_file.readline()
        file_name = file_name.rstrip()
        n = int(read_file.readline())
        read_file.close()

        if n < 0:
            print("Invalid n value, can't proceed further.")
        else:
            if os.path.exists(file_name):
                temp_file = open("temp.txt", "w")
                for _ in range(1, n + 1):
                    temp_file.write(str)

                read_file = open(file_name, "r", encoding="utf8")

                for line in read_file:
                    line = read_file.readline()
                    temp_file.writelines(line)

                read_file.close()
                temp_file.close()

                os.remove(file_name)
                os.rename("temp.txt", file_name)
            else:
                print("File not found.")
    else:
        print("Unable to open input file")


# (e)Read a string x, file name y  an integer n. Insert  x  after the line number n in the file y.
def appendAtMiddle():

    if os.path.exists("001_e_input.txt"):

        read_file = open("001_e_input.txt", "r")
        str = read_file.readline()
        file_name = read_file.readline()
        file_name = file_name.rstrip()
        n = int(read_file.readline())
        read_file.close()

        if n < 0:
            print("Invalid n value, can't proceed further.")
        else:
            if os.path.exists(file_name):
                read_file = open(file_name, "r", encoding="utf8")
                temp_file = open("temp.txt", "w")

                for _ in range(1, n + 1):
                    line = read_file.readline()
                    temp_file.writelines(line)

                temp_file.write(str)

                for line in read_file:
                    line = read_file.readline()
                    temp_file.writelines(line)

                read_file.close()
                temp_file.close()

                os.remove(file_name)
                os.rename("temp.txt", file_name)
            else:
                print("File not found.")
    else:
        print("Unable to open input file")


# driver code
readFirstNLines()
readLastNLines()
appendAtLast()
appendAtBegin()
appendAtMiddle()
