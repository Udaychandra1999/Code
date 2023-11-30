def maxAlternatingSum(nums):
    n = len(nums)
    even_sum = odd_sum = 0
    for num in nums:
        even_sum, odd_sum = max(even_sum, odd_sum - num), max(odd_sum, even_sum + num)
    
    return max(even_sum, odd_sum)

nums = list(map(int, input().split()))
output = maxAlternatingSum(nums)
print("Exercise-1 Output:", output)

