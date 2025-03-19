import sys
import heapq

# Read input
N = int(input().strip())  # Number of people
people = []

# Read N people's coordinates
for _ in range(N):
    x, y = map(int, input().split())
    distance = x**2 + y**2  # Use squared distance to avoid sqrt computation
    people.append((distance, x, y))  # Store distance along with coordinates

K = int(input().strip())  # Number of closest people to find

# Get the K closest people using a min-heap
closest_people = heapq.nsmallest(K, people)

# Print the coordinates of K closest people
for _, x, y in closest_people:
    print(x, y)
