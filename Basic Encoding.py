from collections import defaultdict

# Function to process the queries and compute the required difference
def process_queries(Q, queries):
    # Dictionary to store the frequency of each number
    freq_map = defaultdict(int)
    
    # Process each query to update the frequency map
    for query in queries:
        A, B = query
        freq_map[B] += A
    
    # Now, find the minimum and maximum frequency
    min_freq = float('inf')
    max_freq = -float('inf')
    min_num = float('inf')
    max_num = -float('inf')
    
    # Traverse through the frequency map to calculate min/max frequencies
    for num, freq in freq_map.items():
        if freq < min_freq:
            min_freq = freq
            min_num = num
        elif freq == min_freq:
            min_num = min(min_num, num)
        
        if freq > max_freq:
            max_freq = freq
            max_num = num
        elif freq == max_freq:
            max_num = max(max_num, num)
    
    # The result is the absolute difference between the max and min frequency numbers
    return abs(max_num - min_num)

# Main function to handle input and call the processing function
def main():
    # Reading input
    Q = int(input())  # Number of queries
    queries = []
    
    for _ in range(Q):
        A, B = map(int, input().split())  # Read each query
        queries.append((A, B))
    
    # Process the queries and get the result
    result = process_queries(Q, queries)
    
    # Output the result
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
