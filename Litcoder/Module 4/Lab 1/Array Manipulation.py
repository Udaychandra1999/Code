def mix_the_array(array_size, queries):
    array = [0] * array_size

    for query in queries:
        start, end, value = query
        for i in range(start - 1, end):
            array[i] += value

    return max(array)

array_size_input = int(input())
query_count_input = int(input())
queries_input = [list(map(int, input().split())) for _ in range(query_count_input)]


result = mix_the_array(array_size_input, queries_input)
print(result)