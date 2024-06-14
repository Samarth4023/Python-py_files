# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------


# The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
# Function Description
# Complete the rangoli function in the editor below.
# rangoli has the following parameters:
# int size: the size of the rangoli
# Returns
# string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
# Input Format
# Only one line of input containing size, the size of the rangoli.

def print_rangoli(s):
    # your code goes here
    ab='abcdefghijklmnopqrstuvwxyz'
    mid=((n+(n-1))*2)-1
    rev=[]
    for i in range(s):
        r=''
        k=''
        for j in range(i+1):
            if j==i:
                r+=ab[s-1-j]
                top=r+k[::-1]
                t=top.center(mid,"-")
                rev.append(t)
                print(t)
            else:
                r+=ab[s-1-j]+"-"
                k=r
    for i in range(s-1):
        print(rev[s-2-i])
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)