# 4. Write a program that calculates the volume of a sphere given its radius.

#importing math library
import math

# Function to calculate the volume of a sphere
def calculate_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume


# Input: radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume
volume = calculate_volume(radius)

# Output: display the volume
print(f"The volume of the sphere is: {volume:.2f}")
