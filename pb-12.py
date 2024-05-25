# 12. Write a program that calculates the factorial of a number.

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Input: number to calculate the factorial
n = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(n)

# Output: display the factorial
print(f"The factorial of {n} is: {fact}")
