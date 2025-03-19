def find_flower_indices(n, t, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Total types of flowers
        t (int): Total number of flowers needed
        arr (list): List of integers representing the flowers
    Returns:
        tuple: A tuple containing two integers representing the indices of the flowers
    """
    i=0
    j=n-1
    while(i<=j):
        if arr[i]+arr[j]==t:
            return(i,j)
        elif arr[i]+arr[j]>t:
            j-=1
        else:
            i+=1
    return(-1)



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    t = int(data[1])  # Second input is the integer t
    arr = list(map(int, data[2:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = find_flower_indices(n, t, arr)
    
    # Print the result
    print(result[0], result[1])

if __name__ == "__main__":
    main()
