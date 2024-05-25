# 17. Write a program that reverses a given number.

# Function to reverse a given number
def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    return reversed_number

# Input: number to be reversed
number = int(input("Enter a number: "))

# Reverse the number
reversed_num = reverse_number(number)

# Output: display the reversed number
print(f"The reversed number is: {reversed_num}")
