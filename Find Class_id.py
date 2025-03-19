import sys

# Function declaration
def peakIndexInMountainArray(A):
    """
    Finds the first peak index in a mountain array.
    """
    for i in range(1, len(A) - 1):
        if A[i] >= A[i - 1] and A[i] >= A[i + 1]:
            return i
    return len(A) - 1  # Return last index if it's the highest peak

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(peakIndexInMountainArray(arr))
