# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i e B, you add -1 to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and ,B respectively.
# Enter your code here. Read input from STDIN. Print output to STDOUT.


n, m = map(int, input().split())
arr = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
ini_happ = 0
for x in arr:
    if x in set_A:
        ini_happ = ini_happ + 1
    elif x in set_B:
        ini_happ = ini_happ - 1
    else:
        pass
print(ini_happ)
