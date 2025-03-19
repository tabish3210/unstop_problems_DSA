def longest_palindromic_substring_length(s: str) -> int:
    # Transform s to handle even-length palindromes
    transformed = '#' + '#'.join(s) + '#'
    n = len(transformed)
    p = [0] * n  # p[i] = length of the palindrome radius around i
    center = right = 0
    max_length = 0

    for i in range(n):
        mirror = 2 * center - i  # Mirror index of i around center
        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand palindrome centered at i
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary if expanded past right
        if i + p[i] > right:
            center, right = i, i + p[i]

        # Update maximum palindrome length
        max_length = max(max_length, p[i])

    return max_length


# Driver code
if __name__ == "__main__":
    N = int(input().strip())
    S = input().strip()
    print(longest_palindromic_substring_length(S))
