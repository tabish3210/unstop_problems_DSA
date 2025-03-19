b = input()  # Bob's input
a = input()  # Alice's input

# Function to process a string with backspace ('#')
def process_string(s):
    result = []
    for char in s:
        if char == '#':
            if result:  # If there's something in the result, pop the last character
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

# Process both Bob's and Alice's strings
bob_final = process_string(b)
alice_final = process_string(a)

# Check if the final processed strings are the same
if bob_final == alice_final:
    print("YES")
else:
    print("NO")
