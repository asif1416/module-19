# Factorial
def factorial(n):
    '''This is a recursive function to find factorial of a number'''
    if n == 0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))   
print(factorial(2))    
print(factorial(1))    
print(factorial(15))    
