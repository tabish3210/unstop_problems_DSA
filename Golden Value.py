# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculateGoldenValue(N, Arr):
    # To store the cumulative XOR up to each index
    xor_cumulative = [0] * (N + 1)
    
    # Calculate cumulative XORs
    for i in range(1, N + 1):
        xor_cumulative[i] = xor_cumulative[i - 1] ^ Arr[i - 1]
    
    # To track the sum of XORs of even-length subarrays and odd-length subarrays
    SE = 0  # Sum of XORs for even-length subarrays
    SO = 0  # Sum of XORs for odd-length subarrays
    
    # Loop through the array and calculate the XOR sums
    for i in range(N):
        # If i is the start of a subarray
        for j in range(i + 1, N + 1):
            subarray_xor = xor_cumulative[j] ^ xor_cumulative[i]
            length = j - i
            
            if length % 2 == 0:
                SE += subarray_xor  # Even-length subarrays
            else:
                SO += subarray_xor  # Odd-length subarrays
    
    # The golden value is the absolute difference
    return abs(SE - SO)

# Input
N = int(input())  # Length of the array
Arr = list(map(int, input().split()))  # Array elements

# Output the Golden value
print(calculateGoldenValue(N, Arr))
