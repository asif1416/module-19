# Trigonometric Value
import math

# Get the angle in degrees from the user
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert the angle to radians
angle_radians = math.radians(angle_degrees)

# Calculate the values of trigonometric functions
sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)
cosecant = 1 / sine
secant = 1 / cosine
cotangent = 1 / tangent

# Print the results
print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)
print("Cosecant:", cosecant)
print("Secant:", secant)
print("Cotangent:", cotangent)