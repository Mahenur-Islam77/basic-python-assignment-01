# 16. Write a program that finds the sum of all even numbers between 1 and `n`.
# Function to find the sum of all even numbers between 1 and n
def sum_of_even_numbers(n):
    sum_even = 0
    for i in range(2, n + 1, 2):
        sum_even += i
    return sum_even


# Input: value of n
n = int(input("Enter the value of n: "))

# Calculate the sum of even numbers
sum_even = sum_of_even_numbers(n)

# Output: display the sum
print(f"The sum of all even numbers between 1 and {n} is: {sum_even}")
