# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.

def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1  # Move to the next character after the current match
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)