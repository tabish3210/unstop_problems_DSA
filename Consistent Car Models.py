def count_consistent_cars(components, models):
    allowed_set = set(components)
    count = 0
    
    for model in models:
        if all(char in allowed_set for char in model):
            count += 1
    
    return count

# Input handling
def main():
    components = input().strip()  # Read allowed components
    n = int(input().strip())  # Read number of models
    models = input().split()  # Read models as a list of strings
    print(count_consistent_cars(components, models))

if __name__ == "__main__":
    main()
