def zero_filled_subarray(nums):
    ans = 0
    index_before_zero = -1

    for i in range(len(nums)):
        if nums[i]:
            index_before_zero = i
        else:
            ans += i - index_before_zero

    return ans

# Take user input for the list of numbers
nums_example = list(map(int,input().split()))

result_example = zero_filled_subarray(nums_example)
print(result_example)