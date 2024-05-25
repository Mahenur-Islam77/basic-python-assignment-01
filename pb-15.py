# 15. Write a program that prints the multiplication table of a given number.

# Function to print the multiplication table of a given number
def print_multiplication_table(number, limit=10):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")


# Input: number to print the multiplication table for
number = int(input("Enter the number: "))
limit = int(input("Enter the limit for the multiplication table: "))

# Print the multiplication table
print(f"Multiplication table for {number}:")
print_multiplication_table(number, limit)
