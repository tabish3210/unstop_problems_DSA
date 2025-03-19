def erase_overlap_intervals(intervals):
    """
    Returns the minimum number of intervals to remove to make the rest non-overlapping.
    Parameters:
        intervals (list): List of intervals where each interval is [start, end]
    Returns:
        int: Minimum number of intervals to remove
    """
    if not intervals:
        return 0
    
    # Sort intervals based on the end time
    intervals.sort(key=lambda x: x[1])
    
    end = float('-inf')
    count = 0
    
    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]  # Update the end to the current interval's end
        else:
            count += 1  # Overlapping interval found, increase removal count
    
    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])  # Always 2
    intervals = []
    index = 2
    for _ in range(N):
        intervals.append([int(data[index]), int(data[index + 1])])
        index += 2
    
    result = erase_overlap_intervals(intervals)
    print(result)


if __name__ == "__main__":
    main()
