def findMaxLength(nums):
    sum_dict = {0: -1}
    max_length = 0
    running_sum = 0

    for i in range(len(nums)):
        running_sum += 1 if nums[i] == 1 else -1

        if running_sum in sum_dict:
            max_length = max(max_length, i - sum_dict[running_sum])
        else:
            sum_dict[running_sum] = i

    return max_length

nums = list(map(int, input().split()))
print(findMaxLength(nums))