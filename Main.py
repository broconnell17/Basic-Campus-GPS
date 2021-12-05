"""Setting up a function to grab necessary information to be able to give directions to user.
This will later be used,as well as other information to give basic directions around campus."""
__author__ = "Brendan O'Connell"

import time


def directions():
    """This functions purpose is to take the current location of students as well as taking the academic building they
    need to get to and giving directions to said academic buildings."""
    valid = True
    while valid:
        try:
            print("\n\n\n1.) Academic Services")
            print("\n2.) Academic Halls")
            needed_location = int(input("\nWhich type of building are you trying to find? "))
            if needed_location == 2:
                print("\n1.) Lutgert")
                time.sleep(.5)
                print("\n2.) Holmes ")
                time.sleep(.5)
                print("\n3.) Seidler ")
                time.sleep(.5)
                print("\n4.) Marieb ")
                time.sleep(.5)
                print("\n5.) Sugden ")
                time.sleep(.5)
                print("\n6.) Whitaker ")
                time.sleep(.5)
                print("\n7.) Reed ")
                time.sleep(.5)
                print("\n8.) Griffin ")
                time.sleep(.5)
                print("\n9.) Merwin ")
                time.sleep(.5)
                print("\n10.) Edwards ")
                time.sleep(.5)
                hall_choice = int(input("\nWhich academic hall are you searching for? "))
                print("\n1.) Parking Garage 1")
                time.sleep(.5)
                print("\n2.) Parking Garage 2")
                time.sleep(.5)
                print("\n3.) Parking Garage 3")
                time.sleep(.5)
                print("\n4.) Parking Garage 4")
                time.sleep(.5)
                parking_locaton = int(input("\nWhich parking garage are you in or nearest to? "))
                valid_inputs = True
                while valid_inputs:
                    if hall_choice == 1:  # Lutgert
                        if parking_locaton == 1:
                            print("\nExit the Garage towards the only open pathway (Currently due to construction.) "
                                  "Follow the walkways until you get to The Great Lawn. Once there go straight between"
                                  "the buildings until you reach the last building.")
                            break
                        elif parking_locaton == 2:
                            print("\nExit the garage and head towards the modular buildings. From there you will find"
                                  "a boardwalk. Once across, turn left. The last builing is Lutgert. ")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, and start to walk across the boardwalk. Once you get"
                                  "to the end, take a right. It will be the last building. ")
                            break
                        elif parking_locaton == 4:
                            print("\nExit the parking garage on the side closest to the main road. The building "
                                  "closest to main road is Lutgert. ")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 2:  # Holmes
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, walk through the building in front of you to get to the"
                                  "center of campus. Take a right, and it should be connected to the marketplace. ")
                            break
                        elif parking_locaton == 4:
                            print("\nExit the parking garage towards the two nearest buildings. Go through the gap,"
                                  "and Holmes should be the one connected to the marketplace. ")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 3:  # Seidler
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, and start to walk across the boardwalk. Once you get"
                                  "to the end, go through the building at the end. Look to your right and it will be"
                                  "the building with the large curved deck. ")
                            break
                        elif parking_locaton == 4:
                            print("\nExit the parking garage towards the two nearest buildings. Go through the gap,"
                                  "and look for the building with the large curved deck. ")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 4:  # Marieb
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, and start to walk across the boardwalk. Once you get"
                                  "to the end, take a right. It should be the 1st building adjacent to the parking "
                                  "garage. ")
                            break
                        elif parking_locaton == 4:
                            print("\nExit the garage closer towards the back side, opposite from the entrance, and "
                                  "look for a little turf lawn. That will lead you to an entrance to Marieb. ")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 5:  # Sugden
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("Exit the west side of the parking lot, towards lot 5, and continue past the"
                                  "bookstore/Cohen Center. It will be the building after that")
                            break
                        elif parking_locaton == 4:
                            print("hello")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 6:  # Whitaker
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, and start to walk across the boardwalk. Once you get"
                                  "to the end, go throught the building in front of you. Once you are through, and"
                                  "outside again it will be the building in front of you. ")
                            break
                        elif parking_locaton == 4:
                            print("hello")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 7:  # Reed
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage, and start to walk across the boardwalk. Once you get"
                                  "to the end, take a left. There will be a gap between buildings not to far "
                                  "after. Go through there and it will be the building across the center of the"
                                  "campus, closest to The Great Lawn. ")
                            break
                        elif parking_locaton == 4:
                            print("hello")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 8:  # Griffin
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage and walk across the boardwalk. It is the building "
                                  "directly to the left of the building that will be in front of you once you exit the"
                                  "boardwalk. ")
                            break
                        elif parking_locaton == 4:
                            print("hello")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 9:  # Merwin
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage and walk across the boardwalk. It is the building "
                                  "directly outside of the exit. ")
                            break
                        elif parking_locaton == 4:
                            print("hello")
                            break
                        else:
                            print("\nInvalid. Try again")
                            break
                    elif hall_choice == 10:  # Edwards
                        if parking_locaton == 1:
                            print("HI")
                            break
                        elif parking_locaton == 2:
                            print("Hi")
                            break
                        elif parking_locaton == 3:
                            print("\nExit the parking garage and walk across the boardwalk. It is the building "
                                  "directly to the right of the building that will be in front of you once you exit the"
                                  "boardwalk. ")
                            break
                        elif parking_locaton == 4:
                            print(" ")
                            break
                        else:
                            print("\nInvalid input")
                            break
                    else:
                        print("The number you inputted is not one in the list. Retry. ")
            else:
                print("Invalid. Try Again. ")
            break
        except ValueError:
            print("\nYour input was not accepted as it was not a shown option. ")


# Final message telling user that either inputs weren't accepted, or we don't know the route.
# Directing them to FGCU website to help with building names

def credits_acquired(semesters):
    """This function is to get some more information on the student. It uses semesters and credits to determine
    how far a student is in their college career.
    semesters = amount of semesters a student has been in school, as well as total credits."""
    valid_input = True
    while valid_input:
        try:
            current_credits = int(input("\nHow many credits are you taking this semester? "))
            overall_credits = 0
            for x in range(1, semesters):
                credit_per_semester = int(input("\nHow many credits did you take in your " + str(x) + " semester? "))
                overall_credits += credit_per_semester
            print("\nAfter this semester you will have " + str(overall_credits + current_credits))
            break
        except ValueError:
            print("Try to respond again. Remember to answer in the amount of semesters you have finished. "
                  "It should be a whole number.")



def time_as_student(name):
    """This function gets basic information from the student, just to build an idea of who they are by getting
    information about how long they have been a student, as well as how many credits they are taking.
    """
    valid_input = True
    print("\nHello", name + ".", sep='  ')
    while valid_input:
        try:
            semesters = int(input("\nWhat semester of college are you in? Please respond in amount of semesters. "))
            while semesters:
                if semesters < 0:
                    print("\nAmount of semesters invalid. Please input another amount. ")
                    semesters = int(input("\nHow long have you been at FGCU? Please respond in amount of semesters. "))
                elif 0 <= semesters <= 2:
                    print("\nWelcome", name + ".\n\nIt seems that you are a freshman.")
                    break
                elif 2 <= semesters <= 4:
                    print("\nWelcome", name + ".\n\nIt seems that you are a sophomore.")
                    break
                elif 4 <= semesters <= 6:
                    print("\nWelcome", name + ".\n\nIt seems that you are a junior.")
                    break
                elif 6 <= semesters <= 8:
                    print("\nWelcome", name + ".\n\nIt seems that you are a senior.")
                    break
                else:
                    print("Either your input was negative, or you are beyond your first for years.")
                    break
            credits_acquired(semesters)
            break
        except ValueError:
            print("\nTry to respond again. Remember to answer in the amount of semesters you have finished "
                  "plus the one you are in. It should be a whole number.")


# Function which takes user data, such as credits and time here and breaks it down

def math():
    """
Just a basio demonstration that I know how to use math operators.
    """
    num1 = int(input("\nGive a number. "))
    num2 = int(input("\nGive a second number. "))
    pos_neg(num1, num2)
    print("\nChoices are:")
    time.sleep(.5)
    print("   Addition ")
    print("   Subtraction ")
    print("   Division ")
    print("   Multiplication ")
    typeOfMath = input("\nWhat basic operation would you like to do? ")
    if typeOfMath.upper() == "ADDITION":
        print(num1 + num2)
        return
    elif typeOfMath.upper() == "SUBTRACTION":
        print(num1 - num2)
        return
    elif typeOfMath.upper() == "DIVISION":
        print(" With Decimal:", num1 / num2)
        print(" Without Decimal:", num1 // num2)
        print(" Remainder:", num1 % num2)
        return
    elif typeOfMath.upper() == "MULTIPLICATION":
        print(" Normal Multiplication:", num1 * num2)
        print(" Exponents:", num1 ** num2)
        return
    else:
        print("Invalid input! ")


# Basic math opperations just to fill time after recieving directions.

def pos_neg(num1, num2):
    """
This is a continuation of the math function, and it determines if the numbers you have inputted are positive or
negative.
    """
    if num1 >= 0 and num2 >= 0:
        print("\nBoth numbers are positive! ")
    elif num1 >= 0 or num2 >= 0:
        print("\nOne of your numbers are positive! ")
    elif not (num1 >= 0 and num2 >= 0):
        print("\nBoth numbers are negative! ")


def fun():
    """
This is where the previous two functions incorporate in, as a way to show my knowledge.
    """
    decision = input("\nNow that you know you're directions would you like to partake in a demonstration of math? ")
    if decision.lower() == "yes":
        math()
    elif decision.lower() != "yes":
        print("\nOkay. Thank you again for using our program.")
    else:
        print("\nOkay. Thank you again for using our program.")


def main():
    """
This is where I have compiled all of my functions into one main running function.
    """
    user = input("\nHello! Welcome to this introductory direction program. What is your name? ")
    time_as_student(user)
    time.sleep(2)
    directions()
    fun()


main()
