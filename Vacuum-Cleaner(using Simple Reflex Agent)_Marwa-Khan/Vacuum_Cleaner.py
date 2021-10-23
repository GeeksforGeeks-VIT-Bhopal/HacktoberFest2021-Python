
import random  # to get random value at runtime

location = input("Enter the location of room either A or B:")
room_condition_for_A = random.randint(0, 1)  # 1 means dirty and 0 means clean
print("The room location A is", room_condition_for_A)
room_condition_for_B = random.randint(0, 1)
print("The room location B is", room_condition_for_B)


if location == "A":

    if room_condition_for_A == 0:
        print("\nThe room location ", location, " is already clean")
        print("\nMoving to location B....")

        if room_condition_for_B == 0:
            print("\nThe room location B is already clean\n")
            print("The whole room is cleaned now")

        else:
            print("\nThe location B is dirty,cleaning it")
            print("The location B is cleaned now\n")
            print("The whole room is cleaned now")

    if room_condition_for_A == 1:
        print("\nThe room location ", location, " is dirty,cleaning it")
        print("Room location ", location, " is cleaned now")
        print("\nMoving to location B....\n")

        if room_condition_for_B == 0:
            print("\nThe room location B is already clean\n")
            print("\nThe whole room is cleaned now")

        else:
            print("\nThe location B is dirty,cleaning it")
            print("The location B is cleaned now\n")
            print("\nThe whole room is cleaned now")


elif location == "B":
    if room_condition_for_B == 0:
        print("\nThe room location ", location, " is already clean\n")
        print("\nMoving to location A....")

        if room_condition_for_A == 0:
            print("\nThe room location B is already clean\n")
            print("The whole room is cleaned now")
        else:
            print("The location A is dirty,cleaning it")
            print("The location A is cleaned now\n")
            print("\nThe whole room is cleaned now")

    if room_condition_for_B == 1:
        print("\nThe room location ", location, " is dirty,cleaning it\n")
        print("Room location ", location, " is cleaned now\n")
        print("Moving to location A....\n")

        if room_condition_for_A == 0:
            print("\nThe room location A is already clean\n")
            print("\nThe whole room is cleaned now")

        else:
            print("The location A is dirty,cleaning it")
            print("The location A is cleaned now\n")
            print("\nThe whole room is cleaned now")


else:
    print("Wrong input entered")


