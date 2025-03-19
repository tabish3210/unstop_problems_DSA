def count_set_bits(N):
    total_ones = sum(bin(i).count('1') for i in range(1, N+1))
    return total_ones

# Taking input and printing output
N = int(input().strip())
print(count_set_bits(N))
