def count_subarrays(nums, k):
    if not nums:
        return 0

    n = len(nums)
    count = 0
    left = 0
    product = 1

    for right in range(n):
        product *= nums[right]

        while product >= k and left <= right:
            product /= nums[left]
            left += 1

        count += (right - left + 1)

    return count

nums_str = input()
nums = list(map(int, nums_str.split()))

k = int(input())

result = count_subarrays(nums, k)
print(result)