# 13. Write a program that generates a Fibonacci sequence of length `n`.

# Function to generate a Fibonacci sequence of length n
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence


# Input: length of the Fibonacci sequence
n = int(input("Enter the length of the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(n)

# Output: display the Fibonacci sequence
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_sequence}")
