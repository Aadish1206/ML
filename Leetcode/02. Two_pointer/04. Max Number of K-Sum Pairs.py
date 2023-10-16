def maxOperations(nums, k):
    
    left = 0
    right = len(nums) - 1
    multiply = 0

    while left < right:
        sum = nums[left] + nums[right]
        #print(sum)

        if sum == k:
            multiply += 1
            left += 1
            right -= 1
        elif sum < k:
            left += 1
        else:
            right -= 1

    return multiply


nums = [1, 2, 3, 4]
k = 5
print(maxOperations(nums, k))  

nums = [3,1,3,4,3]
k = 6
print(maxOperations(nums, k))  
