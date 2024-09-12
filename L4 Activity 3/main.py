#Bye bye
valid = False

while not valid:  # Using nested while loop
    try:
        n = int(input("Enter a number: "))
        # Enter an even number
        while n % 2 == 0:
            print("bye")
            valid = True
    except ValueError:
        print("Invalid")