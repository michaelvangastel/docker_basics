#!/usr/bin/python3
import math  # We import an external library to use its functions
import sys


def main(argv):
    try:  # This is a try statement used to handle errors
        # This is a variable which stores the value a user enters
        answer = int(argv[0])
        first = int(argv[1])

        if(answer < 5):
            second = int(argv[2])

        if answer == 1:  # Basic if statement - if user entered 1 then do what's next
            final = first + second
            print("Answer:", float(final))
            print
        elif answer == 2:
            final = first - second
            print("Answer:", float(final))
            print
        elif answer == 3:
            final = first / second
            print("Answer:", float(final))
            print
        elif answer == 4:
            final = first * second
            print("Answer:", float(final))
            print
        elif answer == 5:
            final = first * first
            print("Answer:", float(final))
            print
        elif answer == 6:
            final = math.sqrt(first)
            print("Answer:", float(final))
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


if __name__ == "__main__":
    main(sys.argv[1:])
