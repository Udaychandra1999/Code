def findMin(nums):
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        # If the mid element is greater than the last element, search in the right half
        if nums[mid] > nums[high]:
            low = mid + 1
        # If the mid element is less than or equal to the last element, search in the left half
        else:
            high = mid

    return nums[low]

user_input = input()
nums = list(map(int, user_input.split()))

output = findMin(nums)

print(output)
