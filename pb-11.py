# 11. Write a program that prints the first `n` natural numbers.

# Function to print the first n natural numbers
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ',)
    print()  # For a new line after printing all numbers


# Input: number of natural numbers to print
n = int(input("Enter the value of n: "))

# Print the first n natural numbers
print(f"The first {n} natural numbers are:")
print_natural_numbers(n)
