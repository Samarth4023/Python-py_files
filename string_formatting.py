# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print
# Prints
# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

# Input Format
# A single integer denoting .

def print_formatted(number):
    # your code goes here
    if 1 <= n <= 99:
        for i in range(1, n+1):
            a = i
            b = oct(i)
            c = bin(i)
            d = hex(i)
            A = str(a)
            B = str(b)[2:]
            C = str(c)[2:]
            D = str(d)[2:].upper()
            print(A.ljust(4) + B.ljust(4) + D.ljust(4) + C.rjust(1))
    else:
        print('Please enter value <= 99')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)