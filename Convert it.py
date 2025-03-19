def modify_array(n, arr):
    """
    Modify the array based on the problem statement.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers
    Returns:
        list: Modified array after applying the suggested changes
    """
    modified_arr = []
    max_so_far = 0
    
    for num in arr:
        max_so_far = max(max_so_far, num)
        modified_arr.append(num + max_so_far)
    
    return modified_arr


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the modified array
    modified_arr = modify_array(n, arr)
    
    # Print the modified array
    print(" ".join(map(str, modified_arr)))


if __name__ == "__main__":
    main()






