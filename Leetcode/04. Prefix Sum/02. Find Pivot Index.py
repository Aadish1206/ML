def pivotIndex(nums):
    left_sum = 0
    total = sum(nums)

    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i  # Found the pivot index
        left_sum += nums[i]
        #print(left_sum)

    return -1  


nums = [1, 7, 3, 6, 5, 6]
result = pivotIndex(nums)
print(result)  


