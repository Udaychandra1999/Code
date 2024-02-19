email = input()

# Initialize counters
uppercase_count = 0
lowercase_count = 0
digit_count = 0
other_count = 0

# Iterate through the characters in the email
for char in email:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1

# Calculate percentages
total_chars = len(email)
uppercase_percentage = (uppercase_count / total_chars) * 100
lowercase_percentage = (lowercase_count / total_chars) * 100
digit_percentage = (digit_count / total_chars) * 100
other_percentage = (other_count / total_chars) * 100

# Output
print(f"{uppercase_percentage:.3f}%")
print(f"{lowercase_percentage:.3f}%")
print(f"{digit_percentage:.3f}%")
print(f"{other_percentage:.3f}%")