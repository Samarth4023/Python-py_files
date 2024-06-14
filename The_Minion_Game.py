# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):
    vowels = 'AEOUI'
    N = len(string)
    score_k = 0
    score_s = 0
    for i in range(N):
        if string[i] in vowels:
            score_k += N - i
        else:
            score_s += N - i
    if score_k > score_s:
        print(f"Kevin {score_k}")
    elif score_k < score_s:
        print(f"Stuart {score_s}")
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)