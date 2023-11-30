def mix_array(array_size, queries):
    result = [0] * array_size

    for query in queries:
        start, end, value = query
        result[start - 1] += value
        if end < array_size:
            result[end] -= value

    max_value = 0
    current_sum = 0

    for value in result:
        current_sum += value
        max_value = max(max_value, current_sum)

    return max_value

array_size = int(input())
query_count = int(input())

queries = []
for _ in range(query_count):
    query = list(map(int, input().split()))
    queries.append(query)

output = mix_array(array_size, queries)
print(output)
                                                                                                                            