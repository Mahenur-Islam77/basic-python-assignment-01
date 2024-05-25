# 5. Write a program that finds the average of three numbers.

# Function to calculate the average of three numbers
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

# Input: three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the average
average = calculate_average(num1, num2, num3)

# Output: display the average
print(f"The average of the three numbers is: {average:.2f}")
