from typing import List

def calculate_prefix(nums):
    n = len(nums)
    prefix = [0] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] | nums[i - 1]
    return prefix

def calculate_suffix(nums):
    n = len(nums)
    suffix = [0] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] | nums[i + 1]
    return suffix

def maximumOr(nums, k):
    n = len(nums)
    prefix = calculate_prefix(nums)
    suffix = calculate_suffix(nums)

    # For each num, greedily shift it left by k bits.
    result = max(p | num << k | s for num, p, s in zip(nums, prefix, suffix))
    return result

# Example usage:
nums = list(map(int,input().split()))
k = int(input())
result =maximumOr(nums, k)
print(result)
