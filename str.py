# We will create a simple Python module named str.py that contains utility functions for string manipulation.
def reverse_string(s):
    """Returns the reverse of the input string."""
    return s[::-1]
def is_palindrome(s):
    """Checks if the input string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
def count_vowels(s):
    """Counts the number of vowels in the input string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
def to_uppercase(s):
    """Converts the input string to uppercase."""
    return s.upper()    
def to_lowercase(s):
    """Converts the input string to lowercase."""
    return s.lower()    
def capitalize_string(s):
    """Capitalizes the first letter of each word in the input string."""
    return s.title()
def main():
    test_string = "A man, a plan, a canal: Panama"
    print("Original string:", test_string)  
    print("Reversed string:", reverse_string(test_string))
    print("Is palindrome:", is_palindrome(test_string))
    print("Vowel count:", count_vowels(test_string))
    print("Uppercase string:", to_uppercase(test_string))
    print("Lowercase string:", to_lowercase(test_string))
    print("Capitalized string:", capitalize_string(test_string))
if __name__ == "__main__":
    main()
# End of str.py module