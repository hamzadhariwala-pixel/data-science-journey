# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:   # Base condition
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

# Taking input from user
num = int(input("Enter a number: "))

# Checking if number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("Factorial of", num, "is:", factorial(num))
