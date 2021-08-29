# Last updated by RAJENDRA KUJUR(214161008) on 29-08-2021 at 13:05


# calculates area of a given triangle and returns result
def areaOfTriangle(triangle):

    length = int(triangle[0])
    height = float(triangle[1])
    breadth = float(triangle[2])

    # use Heron's formula for calculating the area
    half_perimiter = (length+height+breadth)/2

    area = (((half_perimiter)*(half_perimiter-length) *
             (half_perimiter-height) * (half_perimiter-breadth))**(0.5))

    return area


# execution begins here
input_list = []
output_list = []


print('For example triangle_1 (1 2 3) and triangle_2 (4 5 6) so our input will look like')
print('1 2 3,4 5 6')
print("Enter Traingle's length, height, breadth separated by single spaces")
print("To enter details for next triangle use comma(,) as a delimter")
input_list = input().split(',')

# for every triangle calculate area and store it back to output_list
for _ in range(len(input_list)):
    triangle = input_list[_].split(' ')

    # pass the triangle string to the function and append result to output_list
    output_list.append(areaOfTriangle(triangle))

# print result
print(output_list)
