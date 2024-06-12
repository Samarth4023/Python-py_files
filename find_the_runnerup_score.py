# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

def find_runner_up_score():
    n = int(input())  # Read the number of participants
    scores = list(map(int, input().split()))  # Read the scores into a list

    # Find the maximum score
    max_score = max(scores)
    
    # Remove all occurrences of the maximum score
    while max_score in scores:
        scores.remove(max_score)
    
    # The runner-up score is now the maximum of the remaining scores
    runner_up_score = max(scores)
    
    print(runner_up_score)

# Call the function
find_runner_up_score()