from itertools import combinations

numbers = [1, 2, 3, 4, 5, 6]

combinations_list = []

# Generate combinations with 1 and in numerical order
for r in range(1, len(numbers) + 1):
    for combo in combinations(numbers, r):
        if 1 in combo:
            combinations_list.append(combo)

# Sort the combinations
combinations_list.sort()

# Print the sorted combinations
for combo in combinations_list:
    print(combo)
