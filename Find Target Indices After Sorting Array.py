def find_target_indices(n, arr, k):
    arr.sort()  # Sorting the array in ascending order
    
    indices = [i for i in range(n) if arr[i] == k]  # Collecting target indices
    
    print(len(indices))  # Printing the count of occurrences
    if indices:
        print(*indices)  # Printing the indices space-separated

# Input Handling
n = int(input())  # Read the size of the array
arr = list(map(int, input().split()))  # Read the array elements
k = int(input())  # Read the target value

find_target_indices(n, arr, k)
