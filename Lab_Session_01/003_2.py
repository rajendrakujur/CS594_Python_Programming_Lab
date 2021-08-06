# Python 3.9.6
# function to print desired output
def print_output(first_number, second_number, y):
    result = first_number/second_number
    # used the concept of round() to print the output upto y(<=16) decimal places
    print(round(result, y))


# execution starts
first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))
y = int(input('Enter y(<=16): '))
# function calling
print_output(first_number, second_number, y)
