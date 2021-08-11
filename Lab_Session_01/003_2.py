# Python 3.9.6


def print_output(first_number, second_number, y):
    if second_number == 0:
        print("Can't divide by zero")
    else:
        result = first_number/second_number
        # if y is zero then only integer part will be used
        if y == 0:
            print(int(result))
        else:
            # Since we have to print exactly y digits so format function for each corresponding y value (<16)
            if y == 1:
                print(format(result, '.1f'))
            elif y == 2:
                print(format(result, '.2f'))
            elif y == 3:
                print(format(result, '.3f'))
            elif y == 4:
                print(format(result, '.4f'))
            elif y == 5:
                print(format(result, '.5f'))
            elif y == 6:
                print(format(result, '.6f'))
            elif y == 7:
                print(format(result, '.7f'))
            elif y == 8:
                print(format(result, '.8f'))
            elif y == 9:
                print(format(result, '.9f'))
            elif y == 10:
                print(format(result, '.10f'))
            elif y == 11:
                print(format(result, '.11f'))
            elif y == 12:
                print(format(result, '.12f'))
            elif y == 13:
                print(format(result, '.13f'))
            elif y == 14:
                print(format(result, '.14f'))
            elif y == 15:
                print(format(result, '.15f'))
            elif y == 16:
                print(format(result, '.16f'))
            else:
                print(format("Overflow so can't print accurate result"))


# execution starts
first_number = int(input('Enter first number : '))
second_number = int(input('Enter second number : '))
y = int(input('Enter y (<=16) : '))
# function calling
print_output(first_number, second_number, y)
