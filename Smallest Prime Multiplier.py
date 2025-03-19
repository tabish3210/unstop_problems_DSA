import math

def find_smallest_multiple(P, N):
    print((P * N) // math.gcd(P, N))

# Read input
P, N = map(int, input().split())
find_smallest_multiple(P, N)
