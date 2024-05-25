# 14. Write a program that checks if a given number is prime or not.

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Input: number to check
n = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(n):
    print(f"The number {n} is a prime number.")
else:
    print(f"The number {n} is not a prime number.")
