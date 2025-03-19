# Read input values
n, k = map(int, input().split())
s = input().strip()

# Reverse the string and find the k-th character
print(s[::-1][k-1])
