#!/usr/bin/python3
'''
Arvin Aya-ay
9-22-20
Haverford Systems Inc. - Application Programmer Python Example Submission
'''
import math

# Prompts user for degrees, ourputs radian value
def deg_to_rad():
    while True:
        try:
            user_in_raw = input(">> Input a Degree (q to return): ")
            if user_in_raw == "q":
                break
            else:
                user_in_float = float(user_in_raw)
                radian_val = math.radians(user_in_float)
                print("Your input in Radians is: " + str(radian_val))
        except ValueError:
            print("Please input a valid Degree")

# Prompts user for radian, outputs degree value
def rad_to_deg():
    while True:
        try:
            user_in_raw = input(">> Input a Radian (q to return): ")
            if user_in_raw == "q":
                break
            else:
                user_in_float = float(user_in_raw)
                degree_val = math.degrees(user_in_float)
                print("Your input in Degrees is: " + str(degree_val))
        except ValueError:
            print("Please input a valid Radian")

# Prompts user for integer, outputs hexadecimal value
def int_to_hex():
    while True:
        try:
            user_in_raw = input(">> Input an Integer (q to return): ")
            if user_in_raw == "q":
                break
            else:
                user_in_int = int(user_in_raw)
                hex_val = hex(user_in_int)
                print("Your input in Hexadecimal is: " + str(hex_val))
        except ValueError:
            print("Please input a valid Integer")

# Prompts user for hexadecimal, outputs integer value
def hex_to_int():
    while True:
        try:
            user_in_raw = input(">> Input a Hexadecimal (q to return): ")
            if user_in_raw == "q":
                break
            else:
                user_in_int = int(user_in_raw, 16) # cast to base 16 int, ie. a hexadecimal
                print("Your input as an Integer is: " + str(user_in_int))
        except ValueError:
            print("Please input a valid Hexadecimal")

# Prints initial program instructions, starts main loop
def main():
    # string to be printed when user types '0' for help
    help_str =\
        "[1] Degree to Radian\n"\
        "[2] Radian to Degree\n"\
        "[3] Integer to Hexadecimal\n"\
        "[4] Hexadecimal to Integer\n"\
        "[5] Exit Program"
    # Print welcome message when program initially launched
    print("\n" + "Welcome to Angle-Hex. Here are the possible commands:\n" + help_str + "\n")

    # Main Loop
    while True:
        try:
            user_in = int(input(">> Please select a command (0 to view commands): "))
            if user_in == 0:
                print(help_str + "\n")
            elif user_in == 1:
                deg_to_rad()
            elif user_in == 2:
                rad_to_deg()
            elif user_in == 3:
                int_to_hex()
            elif user_in == 4:
                hex_to_int()
            elif user_in == 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Command (0 to view list of commands)\n")

# Run program
main()
