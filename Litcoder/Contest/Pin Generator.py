
def generate_pin(numbers):
    def get_single_digit_sum(num):
        while num > 9:
            num = sum(map(int, str(num)))
        return num

    def get_alphabet_char(num):
        return chr(ord('a') + num - 1)

    result = ""
    for num in numbers:
        single_digit_sum = get_single_digit_sum(num)

        if single_digit_sum % 2 == 1:
            result += get_alphabet_char(single_digit_sum)
        else:
            result += str(single_digit_sum)

    return result[:6]

input_numbers = list(map(int, input().split()))

output_pin = generate_pin(input_numbers)
print(output_pin)
                                                                                                                            