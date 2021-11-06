# Brendan O'Connell
# Setting up a function to grab necessary information to be able to give directions to user. This will later be used,
# as well as other information to give basic directions around campus.
def building_directions(needed_location, current_location):
    seidler_inputs = ["SEIDLER", "SEIDLER HALL", "SH"]
    lutgert_inputs = ["LUTGERT", "LUTGERT HALL", "LH"]
    # Using list so that program can take multiple different kinds of inputs
    if needed_location.upper() in seidler_inputs:
        if current_location.upper() == "PARKING GARAGE 4":
            print(
                "\nGo towards the center of campus and look for the building with the curved deck.")
        elif current_location.upper() == "PARKING GARAGE 3":
            print(
                "\nCross boardwalk, walk through the building you come up to, and take a right. You will see Seidler "
                "from there.")
        elif current_location.upper() == "PARKING GARAGE 2":
            print(
                "\nCross boardwalk past the modular buildings, turn left and Seidler Hall should be written on a wall.")
        elif current_location.upper() == "PARKING GARAGE 1":
            print(
                "\nWalk past the Cohen center, or past the lake, towards campus and look for the curved deck.")
        else:
            print(
                "\nLook around for the building that has Seidler Hall written on it.")
    elif needed_location.upper() in lutgert_inputs:
        if current_location.upper() == "PARKING GARAGE 4":
            print(
                "\nWalk towards campus, between the two buildings out from the garage, and look for the building with "
                "glass boxes hanging out the wall.")
        if current_location.upper() == "PARKING GARAGE 3":
            print(
                "\nCross boardwalk, walk through the building you come up to, and take a right. It will be the last "
                "building")
        if current_location.upper() == "PARKING GARAGE 2":
            print(
                "\nCross boardwalk past the modular buildings, then go through the building you come up to and take a "
                "left once through. The last building all the way down is Lutgert")
        if current_location.upper() == "PARKING GARAGE 1":
            print(
                "\nWalk past the Cohen center, or past the lake, towards campus and the last building will be Lutgert.")
        else:
            print(
                "\nFind your way to the pavilion, which will be the grass opening at the end of all the academic"
                " buildings, then walk to the last academic hall. It will be the opposite end of the grass pavilion.")
    else:
        print("\nSorry, Cannot help you find where you are trying to go. You may have inputted names wrong. "
              "Rerun with correct names to get more specific directions")
        print("\nIf you need to find building names or location names, look at the campus map, and then retry. "
              "Double check where you are going. Have a nice day!")
        print("Campus building names can be found at https://" + "w" * 3 +
              ".fgcu.edu/campusreservations/facilities/buildingabbreviations ", end='\n\n :)')


# Final message telling user that either inputs weren't accepted, or we don't know the route.
# Directing them to FGCU website to help with building names

def student_info():
    print("\nHello", user + ".", sep=' ')
    semesters = int(input("\nWhat semester of college are you in? Please respond in amount of semesters. "))
    current_credits = int(input("\nHow many credits are you taking this semester? "))
    while True:
        if semesters < 0:
            print("\nAmount of semesters invalid. Please input another amount. ")
            semesters = int(input("\nHow long have you been at FGCU? Please respond in amount of semesters. "))
        elif 0 <= semesters <= 2:
            print("\nWelcome", user + ".\n\nIt seems that you are a freshman.")
            break
        elif 2 <= semesters <= 4:
            print("\nWelcome", user + ".\n\nIt seems that you are a sophomore.")
            break
        elif 4 <= semesters <= 6:
            print("\nWelcome", user + ".\n\nIt seems that you are a junior.")
            break
        elif 6 <= semesters <= 8:
            print("\nWelcome", user + ".\n\nIt seems that you are a senior.")
            break
    overall_credits = 0
    for x in range(1, semesters):
        credit_per_semester = int(input("\nHow many credits did you take in your " + str(x) + " semester? "))
        overall_credits += credit_per_semester
    print("\nAfter this semester you will have " + str(overall_credits + current_credits) + " credits. ")
# Function which takes user data, such as credits and time here and breaks it down

def math():
    num1 = int(input("\nGive a number. "))
    num2 = int(input("\nGive a second number. "))
    typeOfMath = input("\nWhat basic operation would you like to do? ")
    if typeOfMath.upper() == "ADDITION":
        print(num1 + num2)
    if typeOfMath.upper() == "SUBTRACTION":
        print(num1 - num2)
    if typeOfMath.upper() == "DIVISION":
        print("With Decimal:", num1 / num2)
        print("Without Decimal:", num1 // num2)
        print("Remainder:", num1 % num2)
    if typeOfMath.upper() == "MULTIPLICATION":
        print("Normal Multiplication:", num1 * num2)
        print("Exponents:", num1 ** num2)
    else:
        print("Invalid input! ")
    pos_neg(num1, num2)
# Basic math opperations just to fill time after recieving directions.

def pos_neg(num1, num2):
    if num1 >= 0 and num2 >= 0:
        print("Both numbers are positive! ")
    elif num1 >= 0 or num2 >= 0:
        print("One of your numbers are positive! ")
    elif not (num1 >= 0 and num2 >= 0):
        print("Both numbers are negative! ")


def fun():
    decision = input("\nNow that you know you're directions would you like to partake demonstration of math? ")
    if decision.lower() == "yes":
        math()
    elif decision.lower() != "yes":
        print("Okay. Thank you again for using our program.")


user = input("\nHello! Welcome to this introductory direction program. What is your name? ")
student_info()
current_location = input("\nHello. What is your current location? (Garages, food court, etc.) ")
needed_location = input("\nWhat is the name of the building you are trying to find? (Academic Buildings) ")
building_directions(needed_location, current_location)
fun()
