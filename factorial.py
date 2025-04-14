import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the number from the command-line argument
if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = 5  # Default to 5 if no argument is provided

print(f"The factorial of {num} is {factorial(num)}")

