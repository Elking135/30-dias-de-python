import math
1
def add_two_numbers(a,b):
    return a + b

2
def area_of_circle(r):
    return 3.1416 * r**2

3
def add_all_nums(yea):
    for i in yea:
        yea = yea + 1
        print(yea)

4
def from_celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

5
def check_season(mes):
    if month in ["December", "January", "February"]:
        print("You are in winter")

    elif month in ["March", "April", "May"]:
        print("You are in spring")

    elif month in ["June", "July", "August"]:
        print("You are in summer")

    elif month in ["September", "October", "November"]:
        print("You are in autumn")

8
def print_list(klk):
    klk = []
    for i in klk:
        print(i)

-9
def reverse_list(lis):
    return lis[::-1]
