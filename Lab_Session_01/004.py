# Python 3.9.6


# Program will throw an error if there will be invalid characters
# Do note this program will not check whether the given Roman number is a valid number

# function to print desired output
def lower_to_upper(string):
    switcher = {
        'i': 'I',
        'v': 'V',
        'x': 'X',
        'l': 'L',
        'c': 'C',
        'd': 'D',
        'm': 'M'
    }
    print(switcher.get(string, 'if no cases matched'), end='')


# execution starts
string = input('Enter Roman letters : ')
length = len(string)
# function calling
i = 0
while i < length:
    # Variable to check whether the correct roman symbols are there in string
    string_is_valid = False
    if string[i] == 'i' or string[i] == 'v' or string[i] == 'x' or string[i] == 'l' or string[i] == 'c' or string[i] == 'd' or string[i] == 'm':
        string_is_valid = True
    else:
        # if other than valid 7 characters(i,v,x,l,c,d,m) are there then throw error and exit
        print('Entered wrong characters')
        exit()
    i += 1

i = 0
while i < length and string_is_valid:
    lower_to_upper(string[i])
    i += 1
