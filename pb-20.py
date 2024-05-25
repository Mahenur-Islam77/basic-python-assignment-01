# 20. Write a program that finds the greatest common divisor (GCD) of two numbers.

# Function to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Input: two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
result = gcd(num1, num2)

# Output: display the GCD
print(f"The greatest common divisor (GCD) of {num1} and {num2} is: {result}")
