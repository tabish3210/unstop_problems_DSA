from collections import Counter

def find_repeated_label(num_boxes, labels):
    # Count the frequency of each label
    label_count = Counter(labels)
    
    # Find and return the label that appears exactly n times
    n = num_boxes // 2
    for label, count in label_count.items():
        if count == n:
            return label

# Input reading
num_boxes = int(input())  # This is 2*n
labels = list(map(int, input().split()))

# Output the result
print(find_repeated_label(num_boxes, labels))
