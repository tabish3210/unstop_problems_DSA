def calculate_final_score(ops):
    stack = []
    
    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    
    return sum(stack)

# Input handling
def main():
    n = int(input())  # Read number of operations
    ops = input().split()  # Read operations as a list of strings
    print(calculate_final_score(ops))

if __name__ == "__main__":
    main()
