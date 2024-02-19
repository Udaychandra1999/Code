def longest_substring_length(s):
    char_index = {}  
    start = 0  
    max_length = 0  
    
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  
        char_index[char] = i  
        max_length = max(max_length, i - start + 1)  

    return max_length

# User input
input_string = input()

# Output for the user input
result = longest_substring_length(input_string)
print(result)
                                                                                                                            