def clumsy_factorial(n):
    if n <= 2:
        return n

    result = n * (n - 1) // (n - 2) + (n - 3)
    n -= 4

    while n >= 4:
        result += -n * (n - 1) // (n - 2) + (n - 3)
        n -= 4
    return result - clumsy_factorial(n)

n_input = int(input())

result = clumsy_factorial(n_input)
print(result)