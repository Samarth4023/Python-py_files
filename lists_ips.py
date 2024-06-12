# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())

list = []
for _ in range(N):
    ip = input().split()
    
    if ip[0] == 'print':
        print(list)
    elif ip[0] == 'sort':
        list.sort()
    elif ip[0] == 'pop':
        list.pop()
    elif ip[0] == 'reverse':
        list.reverse()
    elif ip[0] == 'insert':
        list.insert(int((ip[1])), int((ip[2])))
    elif ip[0] == 'append':
        list.append(int((ip[1])))
    elif ip[0] == 'remove':
        list.remove(int((ip[1])))