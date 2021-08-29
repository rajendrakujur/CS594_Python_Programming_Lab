# Last updated by RAJENDRA KUJUR(214161008) on 29-08-2021 at 13:00

# perform square for each element of the list and store it into output list and then prints
def makeSquares(input_list):
    output_list = []
    for _ in range(len(input_list)):
        output_list.append(input_list[_]**2)

    print('\nOutput List : ')
    print(output_list)


# execution begins here
input_list = []
elements = input('Enter list elements separated by single space :\n')
elements = elements.split(' ')
index = 0

while index < len(elements):
    number = int(elements[index])
    input_list.append(number)
    index += 1

# print input list and then print ouput_list
print('Input List : ')
print(input_list)
makeSquares(input_list)
