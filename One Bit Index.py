def count_good_indices(arr):
    def is_power_of_two(x):
        return x > 0 and (x & (x - 1)) == 0

    good_indices = 0
    prefix_sum = 0

    for num in arr:
        prefix_sum += num
        if is_power_of_two(prefix_sum):
            good_indices += 1

    print(good_indices)

# Input handling
N = int(input())  # Read N
arr = list(map(int, input().split()))  # Read array elements
count_good_indices(arr)
