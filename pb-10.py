# Function to calculate the grade based on a given percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 85 and percentage <= 89:
        return "A"
    elif percentage >= 80 and percentage <= 84:
        return "A-"
    elif percentage >= 75 and percentage <= 79:
        return "B+"
    elif percentage >= 70 and percentage <= 74:
        return "B"
    elif percentage >= 65 and percentage <= 69:
        return "C+"
    elif percentage >= 60 and percentage <= 64:  # Fixed range for C
        return "C"
    elif percentage >= 57 and percentage <= 59:
        return "C-"
    elif percentage >= 55 and percentage <= 56:
        return "D+"
    elif percentage >= 51 and percentage <= 54:
        return "D-"
    else:
        return "F"

# Input: percentage
percentage = float(input("Enter the percentage: "))

# Calculate the grade
grade = calculate_grade(percentage)

# Output: display the grade
print(f"The grade for {percentage}% is: {grade}")
