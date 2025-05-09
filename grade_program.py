#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 9th, 2025

# Calculate mark program in python


def calc_mark(level):

    # Initialize new_grade
    new_grade = 0

    # If else to determine grade level, to update new_grade
    if level == "4+":
        new_grade = 98
    elif level == "4":
        new_grade = 91
    elif level == "4-":
        new_grade = 83
    elif level == "3+":
        new_grade = 78
    elif level == "3":
        new_grade = 75
    elif level == "3-":
        new_grade = 71
    elif level == "2+":
        new_grade = 68
    elif level == "2":
        new_grade = 64
    elif level == "2-":
        new_grade = 61
    elif level == "1+":
        new_grade = 58
    elif level == "1":
        new_grade = 54
    elif level == "1-":
        new_grade = 50
    elif level == "0+":
        new_grade = 45
    elif level == "0":
        new_grade = 41
    elif level == "0-":
        new_grade = 37
    else:

        # In the case where invalid input
        new_grade = 101

    # Send back newgrade to the function call
    return new_grade


def main():

    # Get user level
    level_input = input("Enter the level you recieved for this class: ")

    # Get grade percent from function definition of calc_mark
    grade_percent = calc_mark(level_input)

    # Check if a valid grade
    if grade_percent > 100:
        print("You did not enter a valid grade level! You entered", level_input)
    else:
        print("Your grade is", grade_percent, "%")


if __name__ == "__main__":
    main()
