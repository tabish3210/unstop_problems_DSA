def find_max_difference(N, A):
    min_value = A[0]
    max_diff = -1

    for j in range(1, N):
        max_diff = max(max_diff, A[j] - min_value)
        min_value = min(min_value, A[j])

    print(max_diff)

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    find_max_difference(N, A)
