def fourSum(nums, target):
    nums.sort()
    result = []
    
    n = len(nums)
    
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return result

nums_input = input()
target_input = int(input())

# Convert user input to list of integers
nums = list(map(int, nums_input.split()))


result = fourSum(nums, target_input)
for i in result[1:]:
    for j in i:
        print(j,end=" ")
    print()