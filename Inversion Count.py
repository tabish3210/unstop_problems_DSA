from bisect import bisect_left

def count_valid_pairs_optimized(arr):
    arr.sort()
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) <= (arr[i] & arr[j]):
                count += 1

    return count

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output result
print(count_valid_pairs_optimized(arr))
