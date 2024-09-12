# This is the main file for L1 Activity 4
valid = False

while not valid:
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age > 120:
            print("Age is too high.")
        else:
            if age % 2 == 0:
                print("Your age is even.")
            else:
                print("Your age is odd.")
            valid = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")