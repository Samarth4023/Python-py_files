# Task
# You are given a string s.
# Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# Input Format:
# A single line containing a string s.

if __name__ == '__main__':
    s = input()
    alphanumeric = any(char.isalnum() for char in s)
    alphabetical = any(char.isalpha() for char in s)
    digits = any(char.isdigit() for char in s)
    lowercase = any(char.islower() for char in s)
    uppercase = any(char.isupper() for char in s)
    
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)