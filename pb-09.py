# 9. Write a program that determines if a number is positive, negative, or zero.

# Function to determine if a number is positive, negative, or zero
def determine_number_type(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


# Input: number 
number = float(input("Enter a number: "))

# Determine if the number is positive, negative, or zero
result = determine_number_type(number)

# Output: display the result
print(f"The number {number} is {result}.")
