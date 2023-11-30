import itertools

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_special_primes(limit):
    limit -= 1  # To find a number smaller than the input
    digits = [str(i) for i in range(1, 10)]  # Consider digits 1 to 9

    for length in range(1, len(str(limit)) + 1):
        for combination in itertools.product(digits, repeat=length):
            num = int(''.join(combination))
            if num > limit:
                break
            if is_prime(num):
                yield num

def find_largest_special_prime(input_num):
    limit = input_num
    special_primes = list(generate_special_primes(limit))
    return max(special_primes)

# Example usage:
input_num = int(input())
output = find_largest_special_prime(input_num)
print(output)
