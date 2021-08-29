# Last updated by RAJENDRA KUJUR(214161008) on 29-08-2021 at 13:05


# function that performs multiplication in a list from starting_index to last_index and prints result % 7
def performMultiplication(input_list, starting_index, last_index):
    result = 1

    # perform multiplication from starting_index to last_index
    for _ in range(starting_index, last_index+1):
        # everytime perform %97 s that result won't overflow
        result = (result * input_list[_]) % 97

    print(f'Final result : {result}')


# execution begins here
elements = input(
    'Enter list elements separated by single space :\n').split(' ')

index = 0
input_list = []
# convert every element to integer and store it back into list
while index < len(elements):
    input_list.append(int(elements[index]))
    index += 1

starting_index = int(input('Enter starting index of list : '))
last_index = int(input('Enter last index of list : '))

# call the function
performMultiplication(input_list, starting_index, last_index)
