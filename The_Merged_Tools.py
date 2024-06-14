# Complete the merge_the_tools function in the editor below.
# merge_the_tools has the following parameters:
# string s: the string to analyze
# int k: the size of substrings to analyze
# Prints
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.
# Input Format
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i: i+k]
        result = ''
        dic = {}
        for c in s:
            dic[c] = 1 + dic.get(c, 0)
            if dic[c] == 1:
                result += c
        print(result)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)