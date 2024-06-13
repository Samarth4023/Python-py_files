# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

def print_door_mat(N, M):
    pattern = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
    welcome_line = 'WELCOME'.center(M, '-')
    door_mat = pattern + [welcome_line] + pattern[::-1]
    print('\n'.join(door_mat))

if __name__ == '__main__':
    N, M = map(int, input().split())
    print_door_mat(N, M)