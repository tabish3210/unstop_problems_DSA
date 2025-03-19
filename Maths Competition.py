def min_time_to_solve_problems(N, K, A):
    if K == 0:
        return 0  # If no problems need to be solved, time required is 0.
    if N == 0 or max(A) == 0:
        return -1  # No members or all members take infinite time (i.e., Ai = 0).
    
    low, high = 1, K * min(A)  # Binary search range

    def can_solve_in_time(T):
        total_problems = sum(T // ai for ai in A if ai > 0)
        return total_problems >= K

    # Perform binary search
    while low < high:
        mid = (low + high) // 2
        if can_solve_in_time(mid):
            high = mid  # Try a smaller time
        else:
            low = mid + 1  # Increase time

    return low

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

print(min_time_to_solve_problems(N, K, A))
