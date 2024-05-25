# 7. Write a program that finds the maximum of three numbers.


# Function to find the maximum of three numbers
def find_maximum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Input: three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum number
maximum = find_maximum(num1, num2, num3)

# Output: display the maximum number
print(f"The maximum of the three numbers is: {maximum}")
