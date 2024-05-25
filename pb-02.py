# 2. Write a program that calculates the area of a rectangle given its length and width

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width


# Input: length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area(length, width)

# Output: display the area
print(f"The area of the rectangle is: {area}")
