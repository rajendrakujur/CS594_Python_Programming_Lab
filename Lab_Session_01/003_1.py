# Python 3.9.6


# function to print the desired output
def print_output(first_number, second_number):
    if second_number != 0:
        result = first_number/second_number
        # used the concept of format() to print upto 2 decimal digits
        print(format(result, '.2f'))
    else:
        print("Can't divide with zero.")


# execution starts
first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))
# calling function
print_output(first_number, second_number)
