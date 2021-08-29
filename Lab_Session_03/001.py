# Last updated by RAJENDRA KUJUR(214161008) on 29-08-2021 at 12:58

# function to read entire list
from random import randint


def readList(input_list):
    print(input_list)


# function to remove element from a given index
def removeFromList(input_list):
    index = int(input('Enter index which you want to remove : '))

    # if user inuts index out of range
    while index > len(input_list) or index < 0:
        print(f'Enter index between 0 and {len(input_list)}')
        index = int(input('Enter index : '))

    del input_list[index]


# function to insert an element in a givne index
def insertInList(input_list):
    index = int(input('Enter index in which you want to insert : '))

    # if user inuts index out of range
    while index > len(input_list) or index < 0:
        print(f'Enter index between 0 and {len(input_list)}')
        index = int(input('Enter index : '))

    number = int(input('Enter number you want to insert : '))
    input_list.insert(index, number)


# functin to print an element at a given index
def displayAtIndex(input_list):
    index = int(input('Enter index you want to dislay : '))

    # if user inuts index out of range
    while index > len(input_list) or index < 0:
        print(f'Enter index between 0 and {len(input_list)}')
        index = int(input('Enter index : '))

    print(input_list[index])


# main function execution begins here
elements = input('Enter list elements separated by single space :\n')
elements = elements.split(' ')

index = 0
input_list = []
while index < len(elements):
    number = int(elements[index])
    input_list.append(number)
    index += 1

while True:
    # everytime ask user for choices
    print('Which operation you want to perform : ')
    print('(1) Read the list.')
    print('(2) Remove an element from index.')
    print('(3) Insert an element into list at a given index (last index possible).')
    print('(4) Dislay the element at a particular index.')
    print('(5) Exit')
    choice = int(input('Enter choice : '))
    if choice == 1:
        readList(input_list)
    elif choice == 2:
        removeFromList(input_list)
    elif choice == 3:
        insertInList(input_list)
    elif choice == 4:
        displayAtIndex(input_list)
    elif choice == 5:
        break
    else:
        print('Enter valid chice.')
        continue
    print(f'\nUpdated List : \n{input_list}\n\n')
