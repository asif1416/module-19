# Multiple Exceptions
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("Result is:", result)

# Using multiple except blocks for different types of errors
except ZeroDivisionError:
    print("Division by zero is an error!")

except SyntaxError:
    print("Comma is missing. Enter numbers separated by a comma like this: 1, 2")

except Exception:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")
