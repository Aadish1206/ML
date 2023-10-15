def moveZeroes(nums):
    index = 0  # pointer
   
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element to its correct position.
            nums[i], nums[index] = nums[index], nums[i]
            index += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  
