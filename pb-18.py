# 18. Write a program that checks if a given string, is a palindrome.

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and punctuation, convert to lowercase
    s = s.lower().replace(" ", "").strip(".,!?;:-")
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input: string to check
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
