def find_kth_unique_string():
    # Read the number of strings
    N = int(input().strip())
    
    # Dictionary to store frequency of strings and order of first appearance
    freq = {}
    order = []
    
    # Read the strings and track frequency
    for _ in range(N):
        s = input().strip()
        if s not in freq:
            freq[s] = 0
            order.append(s)
        freq[s] += 1

    # Collect unique strings in order of first appearance
    unique_strings = [s for s in order if freq[s] == 1]

    # Read the value of k
    k = int(input().strip())

    # Output the kth unique string if possible
    print(unique_strings[k-1] if k <= len(unique_strings) else -1)

# Function call
find_kth_unique_string()
