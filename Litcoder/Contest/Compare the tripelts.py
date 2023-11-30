def compareTriplets(c, d):
    charlie_points = 0
    dave_points = 0

    for charlie_score, dave_score in zip(c, d):
        if charlie_score > dave_score:
            charlie_points += 1
        elif charlie_score < dave_score:
            dave_points += 1

    return charlie_points, dave_points

# Get user input for Charlie's scores
c = list(map(int, input().split()))

# Get user input for Dave's scores
d = list(map(int, input().split()))

# Calculate and print the result
result = compareTriplets(c, d)
print(result)