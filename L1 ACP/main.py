def calculate_circumference(radius):
    pi = 3.1416
    return 2 * pi * radius

radius = float(input("Enter the radius: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {circumference}")
