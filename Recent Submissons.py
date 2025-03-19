# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

def max_submission_queue(N, arr):
    queue = deque()
    max_size = 0

    for t in arr:
        # Remove outdated submissions (more than 5000 seconds old)
        while queue and queue[0] <= t - 5000:
            queue.popleft()
        
        # Add the new submission
        queue.append(t)

        # Update max size of queue
        max_size = max(max_size, len(queue))

    print(max_size)

# Sample Input Handling
N = int(input().strip())
arr = list(map(int, input().strip().split()))

max_submission_queue(N, arr)
