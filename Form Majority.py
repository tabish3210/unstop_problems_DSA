def find_majority_subsequence(votes):
    votes.sort(reverse=True)  # Sort votes in non-increasing order
    
    total_votes = sum(votes)
    majority_threshold = total_votes / 2
    
    selected_votes = []
    selected_sum = 0
    
    for vote in votes:
        selected_votes.append(vote)
        selected_sum += vote
        
        if selected_sum > majority_threshold:
            break
    
    print(*selected_votes)

# Input handling
n = int(input())  # Read size of votes array
votes = list(map(int, input().split()))  # Read votes

find_majority_subsequence(votes)
