class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_bst(root, start, end):
    if not root:
        return 0
    
    if root.val < start:
        return range_sum_bst(root.right, start, end)
    elif root.val > end:
        return range_sum_bst(root.left, start, end)
    else:
        return root.val + range_sum_bst(root.left, start, end) + range_sum_bst(root.right, start, end)

# Function to insert nodes into the BST
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Input handling
def main():
    n = int(input().strip())  # Number of nodes
    nodes = list(map(int, input().split()))  # Node values
    start, end = map(int, input().split())  # Range values
    
    root = None
    for val in nodes:
        root = insert_into_bst(root, val)
    
    print(range_sum_bst(root, start, end))

if __name__ == "__main__":
    main()
