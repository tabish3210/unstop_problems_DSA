def max_min_pair_sum(n, nums):
    nums.sort()  # Step 1: Sort the array
    max_sum = sum(nums[i] for i in range(0, 2*n, 2))  # Step 2: Sum up min values of adjacent pairs
    print(max_sum)

# Reading input
n = int(input()) // 2  # Since input gives 2N, we divide by 2 to get N
nums = list(map(int, input().split()))

# Function call
max_min_pair_sum(n, nums)
