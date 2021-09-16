# This program is last updated by RAJENDRA KUJUR (214161008) on 15-09-2021 at 22:05

import sys
from vehicles import vehicles
import random


# calculates the distance between two given points and returns the result
def calculateDistance(first_x, first_y, second_x, second_y):
    return (((first_x-second_x)**2+(first_y-second_y)**2)**0.5)


# write the updated list of vehicles onto the list
def updateFile():
    output_file = open('vehicles.py', 'w')
    line = ''
    line += 'vehicles = ['

    output_file.write(line)

    # update all the dictionaries available in the list
    for _ in range(len(vehicles)):
        line = ''
        line += '{'
        line += "'Registration Number' : "
        line += str(vehicles[_]['Registration Number'])
        line += ','
        line += "'x_ordinate' : "
        line += str(vehicles[_]['x_ordinate'])
        line += ','
        line += "'y_ordinate' : "
        line += str(vehicles[_]['y_ordinate'])
        line += ','
        line += "'availability' : "
        line += "'"
        line += str(vehicles[_]['availability'])
        line += "'"
        line += '}'
        if _ < len(vehicles)-1:
            line += ','
        line += '\n'
        output_file.writelines(line)

    output_file.write(']')
    output_file.close()
    print("\nUpdated result can be seen at 'vehicles.py'")


# generates vehicle data list having dictionary of field registration number,co-ordinates and availablity
# and writes to file
def generateVehicleData():
    output_file = open('vehicles.py', 'w')
    number_of_vehicles = int(
        input('Enter number of vehicles you want to generate : '))

    # syntax lines for the output file
    line = 'vehicles = ['

    # to choose randomly when required
    availability = ['free', 'booked']

    output_file.write(line)

    # generate give number of dictionaries
    for _ in range(number_of_vehicles):
        line = ''
        line += '{'
        line += "'Registration Number':"
        line += str(_)
        line += ','
        line += "'x_ordinate' : "
        line += str((random.random()-0.5)*100)
        line += ','
        line += "'y_ordinate' : "
        line += str((random.random()-0.5)*100)
        line += ','
        line += "'availability' :"
        line += "'"
        line += str(random.choice(availability))
        line += "'"
        line += '}'
        if _ < number_of_vehicles-1:
            line += ','
        line += '\n'
        # and add in the output_file
        output_file.writelines(line)

    # at the end close the list
    output_file.write(']')
    print("\nGenerated and written to the file 'vehicles.py'")
    output_file.close()


# adds a new vehicle by taking all the parameters for new vehicle
def addVehicle():

    # prompts for the new vehicle data
    vehicle_number = int(input('Enter vehicle registration number :'))
    x_ordinate = float(input('Enter x ordinate (numbers only) : '))
    y_ordinate = float(input('Enter y ordinate (numbers only) : '))

    # keep asking user to enter valid availablity in case of invalid input
    while True:

        availability = input('free or booked ?').lower()
        # if valid input is given then update the dictionary
        if availability == 'free' or availability == 'booked':
            new_vehicle = {
                'Registration Number': vehicle_number,
                'x_ordinate': x_ordinate, 'y_ordinate': y_ordinate, 'availability': availability
            }
            # at last append the new dictionary into the list
            vehicles.append(new_vehicle)
            # udpate the file
            updateFile()
            break
        else:
            print('Enter a valid availability :')


# removes a vehicle if it is present in vehicles list
def removeVehicle():
    vehicle_number = int(
        input('Enter vehicle registration number which you want to remove :'))

    # to keep track whether the vehicle with given registration number found or not
    flag = False

    # check the vehicles if given vehicle number is present
    for _ in range(len(vehicles)):
        if vehicles[_]['Registration Number'] == vehicle_number:
            del vehicles[_]
            flag = True
            updateFile()
            return

    # if no vehicles data is present
    if len(vehicles) == 0:
        print('\nNo vehicle Data is present')

    # if not present then print the error message
    elif flag == False:
        print(
            f'\nVehicle with Registration number : {vehicle_number} not found.')


# after entering starting and destination co-ordinates user can travel if a cab is free
def travelAfterBooking():

    if len(vehicles) == 0:
        print('No vehicle data is present at the moment try after adding some data.')

    # prompt for starting co-ordinate
    starting_x = float(input('Enter your x co-ordinate (numbers only) : '))
    starting_y = float(input('Enter your y co-ordinate (numbers only) : '))

    # prompt fr destination co-ordinate
    destination_x = float(
        input('Enter your destination x co-ordinate (numbers only) : '))
    destination_y = float(
        input('Enter your destination y co-ordinate (numbers only) : '))

    # update minimum distance to max float value possible
    minimum_distance = sys.float_info.max
    index = -1

    # for each vehicle check
    for _ in range(len(vehicles)):

        # if the vehicle is currently free then
        if vehicles[_]['availability'] == 'free':

            # calculate the distance of vehicle from user
            distance = calculateDistance(
                starting_x, starting_y, vehicles[_]['x_ordinate'], vehicles[_]['y_ordinate'])

            # update minimum distance if lower that already available minimum distance and store the index of vehicle
            if float(distance) < minimum_distance:
                minimum_distance = distance
                index = vehicles[_]['Registration Number']

    # if we found a vehicle available for booking
    if index != -1:
        # show the cab details to the user
        print('\nThe nearest cab available for booking')
        print('Details are as follows : ')
        print(
            f"Registartion Number : {vehicles[index]['Registration Number']}")
        print(
            f"Currently at [{vehicles[index]['x_ordinate']} , {vehicles[index]['y_ordinate']}]")
        print(f"Status : {vehicles[index]['availability']}")

        # prompt if user wants to book or not
        travel = input(
            'Enter yes if you want to travel or any other if not ').lower()

        if travel == 'yes':
            # update vehicle availability since the user in traverling
            vehicles[index]['availability'] = 'booked'
            print(
                f"\nAvailability updated to : {vehicles[index]['availability']}")
            print('Cab is taking you to the destination.')
            updateFile()

            ride_completed = input(
                '\nHave you completed your ride yes/no : ').lower()

            if ride_completed == 'yes':

                # reset the vehicle availability to free since it took the user to destination now free to use
                vehicles[index]['availability'] = 'free'

                # update vehicle location
                vehicles[index]['x_ordinate'] = destination_x
                vehicles[index]['y_ordinate'] = destination_y

                updateFile()
                print(
                    f"\nLocation updated to : [{vehicles[index]['x_ordinate']} , {vehicles[index]['y_ordinate']}]")
                print(
                    f"Availability updated to : {vehicles[index]['availability']}")

            else:
                print('Cab will be remained booked.')

    # if all the vehicles are booked
    else:
        print('\nNo cabs are free currently. Try after some time.')


# main function execution begins here
while True:
    print('\n1.Generate a new vehicle data list randomly')
    print('2.To add a Vehicle')
    print('3.To remove a Vehicle using registration number')
    print('4.To travel after giving your current and destination location')
    print('5.Exit')

    choice = int(input('Enter choice :'))

    if choice == 1:
        generateVehicleData()
    elif choice == 2:
        addVehicle()
    elif choice == 3:
        removeVehicle()
    elif choice == 4:
        travelAfterBooking()
    elif choice == 5:
        break
    else:
        print('Enter valid choice.')
