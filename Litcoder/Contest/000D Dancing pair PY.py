def find_dance_pairs(heights):
    # Check if the input is a list of numbers
    if not all(isinstance(h, int) for h in heights):
        print("Input string was not in a correct format")
        return

    # Check if all heights are equal
    if all(h == heights[0] for h in heights):
        print("No Valid pairs")
        return

    # Check if there's only one dancer
    if len(heights) == 1:
        print("No Valid pairs")
        return

    # Sort the heights to pair tall dancers with short dancers
    heights.sort()

    # Iterate through the sorted heights to form pairs
    for i in range(0, len(heights)//2):
        tall_dancer = heights[-(i+1)]
        short_dancer = heights[i]
        print(f"{tall_dancer} {short_dancer}")

# Taking input from the user
user_input = input()

# Convert input to a list of integers
try:
    heights = [int(h) for h in user_input.split()]
except ValueError:
    print("Input string was not in a correct format")
    exit()

# Call the function to find dance pairs
find_dance_pairs(heights)