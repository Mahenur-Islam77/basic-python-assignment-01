# 8. Write a program that determines if a year is a leap year or not.

# Function to determine if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input: year 
year = int(input("Enter a year: "))

# Determine if the year is a leap year
if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
