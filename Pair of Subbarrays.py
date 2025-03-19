from collections import defaultdict

def find_subarray_pairs(N, A):
    # Map to store prefix sum and list of ending indices where that sum occurs
    prefix_sum = 0
    subarray_sums = defaultdict(list)
    result_count = 0
    
    # Loop through all possible subarrays
    for start in range(N):
        prefix_sum = 0
        # For each subarray starting at 'start', check all subarrays that end at 'end'
        for end in range(start, N):
            prefix_sum += A[end]
            
            # Check if the sum is already in subarray_sums and no overlap occurs
            for prev_end in subarray_sums[prefix_sum]:
                # If the previous end index is less than the current start, they don't overlap
                if prev_end < start:
                    result_count += 1
            
            # Append the current subarray ending index to the prefix_sum list
            subarray_sums[prefix_sum].append(end)
    
    return result_count

def main():
    N = int(input())  # Read size of array
    A = list(map(int, input().split()))  # Read the array elements
    result = find_subarray_pairs(N, A)  # Get the result
    print(result)

if __name__ == "__main__":
    main()
