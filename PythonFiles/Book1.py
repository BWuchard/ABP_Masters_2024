from itertools import combinations

# Set of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Function to generate combinations with 6
def generate_combinations_with_6(numbers, min_length, max_length):
    all_combinations = []
    for length in range(min_length, max_length + 1):
        for combo in combinations(numbers, length):
            if combo[0] == 1 and all(combo[i] - combo[i - 1] == 1 for i in range(1, len(combo))) and 6 in combo:
                all_combinations.append(combo)
    return all_combinations

# Generate combinations from length 3 to 5 with 6 included
combinations_3_to_5_with_6 = generate_combinations_with_6(numbers, 3, 5)

# Print the combinations
for combo in combinations_3_to_5_with_6:
    print(combo)
