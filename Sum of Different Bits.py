def count_differing_bits(a, b):
    a_len, b_len = len(a), len(b)
    total_diff = 0
    
    for i in range(b_len - a_len + 1):
        substring = b[i:i + a_len]
        total_diff += sum(1 for x, y in zip(a, substring) if x != y)
    
    return total_diff

# Input handling
def main():
    a = input().strip()  # Read binary string a
    b = input().strip()  # Read binary string b
    print(count_differing_bits(a, b))

if __name__ == "__main__":
    main()
