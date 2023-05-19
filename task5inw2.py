# Check the following code and apply all of what you learnt this week in program design
# Take decisions on what is not good at this program
# Follow the guidelines you learnt (utility functions, comments, doctsrtings)
# Refactor the whole code and provide a new one that meets proper guidelines
# Code Before Refactor:
import math


# import math
#
# # Read in the coordinates of two points
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))
#
# # Calculate the distance between the two points
# distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#
# # Calculate the slope of the line connecting the two points
# slope = (y2 - y1) / (x2 - x1)
#
# # Calculate the y-intercept of the line connecting the two points
# y_intercept = y1 - slope * x1
#
# # Print the distance, slope, and y-intercept
# print(f"Distance: {distance}")
# print(f"Slope: {slope}")
# print(f"Y-Intercept: {y_intercept}")
# ```
def find_distance(difference_in_X: float, difference_in_Y: float) -> float:
    """
    param difference_in_X(float): this sub of x2-x1
    param difference_in_Y(float): this sub of y2-y1
    return: distance(float)
        the distance between the differance of x1 and x2 and the differance between y1 and y2
    """
    # we use math labriary to use built in function as sqrt
    distance = math.sqrt(difference_in_X.__pow__(2) + difference_in_Y.__pow__(2))
    return distance


def find_slope(difference_in_X: float, difference_in_Y: float) -> float:
    """
    param difference_in_X(float): this sub of x2-x1
    param difference_in_Y(float): this sub of y2-y1
    :return: slope(float):this is return a slope by diviation of differance of y to differance of x
    """
    slope = difference_in_Y / difference_in_X
    return slope


def find_y_intercept(x1: float, y1: float) -> float:
    """
    param x1(float): the x1 was entered from user
    param y1(float): the y1 was entered from user
    return y_intercept(float):the Y_intercept
    """
    y_intercept = y1 - find_slope(differance_in_X, difference_in_Y) * x1
    return y_intercept


# we use try and except to force user enter only float not characters
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    differance_in_X = x2 - x1
    difference_in_Y = y2 - y1
    print("The distance is : ", find_distance(differance_in_X, difference_in_Y))
    print("The slope is : ", find_slope(differance_in_X, difference_in_Y))
    print("The Y_intercept is: ", find_y_intercept(x1, y1))
except ValueError:
    print("Sorry you can't complite this operation must enter float ")
