# Last updated by RAJENDRA KUJUR(214161008) on 18-08-2021 at 20:52
# Python Version: Python 3.9.6
# Editor : Visual Studio Code

# function that prints according to age
def printSomething(age):
    if age < 0 or age > 150:
        print('Unlikely to be the age of a human being')
    elif age == 0:
        print('infant')
    elif age == 1 or age == 2:
        print('toddler')
    elif age > 2 and age < 13:
        print('child')
    elif age >= 13 and age < 30:
        print('teen')
    elif age >= 20 and age < 30:
        print('twenty something')
    elif age >= 30 and age <= 59:
        print('adult')
    elif age > 59 and age < 150:
        print('senior citizen')


# execution begins
age = int(input("Enter a number : "))
printSomething(age)
