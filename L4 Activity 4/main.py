# This is the main file for L1 Activity 4
valid =False
while not valid:
    try:
        n=int(input("Enter a age: "))
        while n%2==0:
            print("bye")
        valid = True
    except ValueError:
        print("Invalid")