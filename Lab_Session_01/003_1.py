# Python 3.9.6
# function to print the desired output
def print_output(first_number, second_number):
    result = first_number/second_number
    # used the concept of round() to print upto 2 decimal digits
    print(round(result, 2))


# execution starts
first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))
# calling function
print_output(first_number, second_number)
