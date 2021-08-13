# Python 3.9.6
# Last updated on 10-08-2021 by Rajendra Kujur (214161008)


# function to print the result of given expression
def print_output(X, Y):
    result = (X**Y)+(Y**X)
    # used the concept of fstring to print result
    print(f'{result}')


# execution starts
X = int(input('Enter X : '))
Y = int(input('Enter Y : '))
# function calling
print_output(X, Y)
