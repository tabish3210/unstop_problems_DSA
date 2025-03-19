import sys
sys.setrecursionlimit(10**6)

def find_longest_path(n, tree):
    # Helper function to perform DFS and return the farthest distance and farthest node
    def dfs(node):
        # If the node has no children, return 0 as the distance
        if node == -1:
            return 0
        left_dist = dfs(tree[node][0])  # Distance through the left child
        right_dist = dfs(tree[node][1])  # Distance through the right child
        
        # The maximum distance from this node is max of left and right subtree plus 1 for the current edge
        max_dist = max(left_dist, right_dist) + 1
        
        # Update the global diameter using the sum of distances from both children
        nonlocal diameter
        diameter = max(diameter, left_dist + right_dist)
        
        return max_dist
    
    # The tree is 1-indexed, so we create a 1-indexed tree with `n+1` size
    tree = [[]] + tree
    diameter = 0
    dfs(1)  # Start DFS from the root (vertex 1)
    return diameter

def main():
    # Read input
    n = int(input())  # Number of landmarks (nodes in the tree)
    tree = []
    
    # Read the binary tree structure
    for i in range(n):
        l, r = map(int, input().split())
        tree.append([l, r])
    
    # Find the longest path in the tree (diameter)
    result = find_longest_path(n, tree)
    
    # Output the result
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()
