# Created by k0r8i05
# Practical Beginner Steps
# Simple Calculator Program
# Complete Command Line ( No GUI Attached )
# Beginner Structure - No Functions and/or Classes
# Limited Error Checking and Conditionals Used
# Time-Stamp: 04-06-16 - 09:34AM - CAT

import math  # We import an external library to use its functions

# This is our on/off switch for the program. True is on and False is off.
active = True

# We make a while loop. So while active(True) - keep repeating everything inside
while active:
    # This is our menu and list options for the user - It's inside a while loop so that the entire program doesn't run once and then exit.
    print("1) Add")
    print("2) Subtract")
    print("3) Divide")
    print("4) Multiply")
    print("5) Squared")
    print("6) Square Root")
    print
    print("0) Exit")

    try:  # This is a try statement used to handle errors
        # This is a variable which stores the value a user enters
        answer = input("Option: ")
        # The input function makes the program wait for user input
        # Input returns integers, so letters and special characters cause errors
        print  # These blank print statements are for neatness

        # Note We Do Not Need To Use If-Else Statements Here But For Simplicities Sake We Are

        if answer == 1:  # Basic if statement - if user entered 1 then do what's next
            # Get the first number from user and store it in the variable 'first'
            first = input("First Number: ")
            # Get the second number from user and store it in the variable 'second'
            second = input("Second Number: ")
            final = first + second  # Create a new variable to hold the sum of 'first' and 'second'
            # We print the answer back to the user as a floating point ( a number with a decimal place i.e 1.0, 44.2 )
            print("Answer:", float(final))
            print
        elif answer == 2:
            first = input("First Number: ")
            second = input("Second Number: ")
            final = first - second
            # We use the ',' instead of '+' because we are trying to use 2 different data types in the same output
            print("Answer:", float(final))
            # We have a string "Answer" and a floating point number or integer.
            # If we done " Hello " + " You " it would work because those are both strings.
            # Anything inside quotations marks becomes a string
            # So to use 2 different data types in the same sentence use a comma to separate them.
            print
        elif answer == 3:
            first = input("First Number: ")
            second = input("Second Number: ")
            final = first / second
            print("Answer:", float(final))
            print
        elif answer == 4:
            first = input("First Number: ")
            second = input("Second Number: ")
            final = first * second
            print("Answer:", float(final))
            print
        elif answer == 5:
            first = input("Number: ")
            final = first * first
            print("Answer:", float(final))
            print
        elif answer == 6:
            first = input("Number: ")
            # Here we use an external function from the Math module which is sqrt ( Square Root )
            final = math.sqrt(first)
            print("Answer:", float(final))
            print
        elif answer == 0:  # This is how we exit the program. We make active go from True to False.
            # This has to do with how we designed the while loop. Since it's dependant on the active variable to run
            active = False
        else:  # This is for if the user enters any number that's not on the list
            print
            print("Please select a valid option number")
            print
    except NameError:  # This is part of the try statement. This is how we handle the errors
        # If it's a NameError - Do this and so on
        # NameError means we entered letters or rather variable names that are not defined in the code.
        print
        print("NameError: Please Use Numbers Only")
        print
    # SyntaxError means we typed letters or special characters i.e !@#$%^&*( or if we tried to run python code
    except SyntaxError:
        print
        print("SyntaxError: Please Use Numbers Only")
        print
    except TypeError:  # TypeError is if we entered letters and special characters or tried to run python code
        print
        print("TypeError: Please Use Numbers Only")
        print
    except AttributeError:  # AttributeError handles rare occurances in the code where numbers not on the list are handled outside of the if statement
        print
        print("AttributeError: Please Use Numbers Only")
        print
