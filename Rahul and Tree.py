# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    """
    Constructs a height-balanced BST from a sorted array.
    """
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preorderTraversal(root):
    """
    Prints pre-order traversal of the BST with required format.
    """
    if not root:
        return
    left_val = str(root.left.val) if root.left else "."
    right_val = str(root.right.val) if root.right else "."
    print(f"{left_val} <- {root.val} -> {right_val}")
    preorderTraversal(root.left)
    preorderTraversal(root.right)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    root = sortedArrayToBST(arr)
    preorderTraversal(root)
