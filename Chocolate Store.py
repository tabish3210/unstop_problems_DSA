from collections import defaultdict
import sys

# Function to process the queries
def process_queries(Q, queries):
    # A defaultdict to store chocolates by type
    chocolates = defaultdict(int)
    
    # List to store the results of type 2 queries
    result = []
    
    # Process each query
    for query in queries:
        query_type, chocolate_type, quantity = query
        quantity = int(quantity)
        
        if query_type == 1:
            # Add chocolates of a certain type
            chocolates[chocolate_type] += quantity
        
        elif query_type == 2:
            # Sell chocolates of a certain type
            available = chocolates[chocolate_type]
            if available >= quantity:
                # If enough chocolates are available, sell as requested
                chocolates[chocolate_type] -= quantity
                result.append(str(quantity))
            else:
                # Otherwise, sell all available chocolates
                chocolates[chocolate_type] = 0
                result.append(str(available))
    
    # Print all results at once for type 2 queries
    sys.stdout.write("\n".join(result) + "\n")

# Main function to read input and call the processing function
def main():
    # Reading input
    Q = int(input())  # Number of queries
    queries = []
    
    for _ in range(Q):
        event = input().split()
        queries.append((int(event[0]), event[1], event[2]))  # query_type, chocolate_type, quantity
        
    # Call the function to process the queries
    process_queries(Q, queries)

# Run the main function
if __name__ == "__main__":
    main()
