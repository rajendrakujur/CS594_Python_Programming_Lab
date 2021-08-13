# Python 3.9.6
# Last updated on 10-08-2021 by Rajendra Kujur (214161008)

# function to print pattern, input taken as a constant as per given in problem statement
def print_pattern(number_of_lines):
    for i in range(number_of_lines):
        # loop to print spaces
        for j in range(i):
            print(' ', end='')
        # loop to print asterisks
        for j in range(1, 2*(number_of_lines-i)):
            print('*', end='')
        # to get into the next line extra print() statement required
        print()


# execution starts
print_pattern(7)
