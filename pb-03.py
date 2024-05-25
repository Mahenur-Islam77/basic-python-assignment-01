# 3.Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius


# Input: temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Output: display the temperature in Celsius
print(f"The temperature in Celsius is: {celsius:.2f}")
