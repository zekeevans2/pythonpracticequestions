

# Q40) Write a python program to calculate the disatance betweent the points (x1, y1) and (x2, y2).

import math

def main():
    while True:
        input1 = input("Please type in the first set of coordinates: ")
        input2 = input("Please type in the second set of coordinates: ")
        
        coords1 = input1.split(',')
        coords2 = input2.split(',')
        
        p1 = try_parse_coords(coords1)
        p2 = try_parse_coords(coords2)
        
        result = (distance_calculator(p1,p2))
        
        print(result)
        
        more_coordinates = input("Do you want to calculate the distance for more coordinates? (y/n): ").lower()
        
        if more_coordinates != "y":
            print("Program closing....")
            break

def try_parse_coords(lst):
    coords = []
    for value in lst:
        try:
            parsed_value = int(value)
            coords.append(parsed_value)
        except ValueError:
            return None
    return coords

def distance_calculator(p1, p2):
    if p1 is None or p2 is None:
        return "Please use ints for your coordinates."
    try:
        distance = math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))
    except ValueError:
        return "Please use units for your coordinates."
    return distance

main()