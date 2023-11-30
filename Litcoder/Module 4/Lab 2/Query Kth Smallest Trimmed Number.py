def kth_smallest_trimmed(nums, queries):
    answer = []
    for query in queries:
        position, trimi = query
        trimmed_nums = [int(num[-trimi:]) for num in nums]

        sorted_indices = sorted(range(len(trimmed_nums)), key=lambda i: trimmed_nums[i])

        kth_index = sorted_indices[position - 1]

        answer.append(str(kth_index))

    return answer

nums_input = input().split()
queries_input = input()
queries = [tuple(map(int, input().split())) for _ in range(int(queries_input))]

result = kth_smallest_trimmed(nums_input, queries)
print(" ".join(result))