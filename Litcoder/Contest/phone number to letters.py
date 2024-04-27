def letter_combinations(digits):
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    def backtrack(index, path):
        
        if index == len(digits):
            result.append(''.join(path))
            return

    
        current_digit = digits[index]
        letters = mapping[current_digit]

        
        for letter in letters:
            path.append(letter)

            backtrack(index + 1, path)
         
            path.pop()

    if not digits:
        return []

    result = []
    backtrack(0, [])

    return result

# User input for the string of digits
input_digits = input()
output = letter_combinations(input_digits)
print(" ".join(output))