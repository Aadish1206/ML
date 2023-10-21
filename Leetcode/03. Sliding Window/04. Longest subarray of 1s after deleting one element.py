def longestSubarray(nums):
    max_length = 0
    current = 0
    zero_index = -1  

    for right in range(len(nums)):
        if nums[right] == 0:
            if zero_index != -1:
                current = zero_index + 1
                #print(current)
            zero_index = right
            #print(zero_index)

        max_length = max(max_length, right - current + 1)
        #print(max_length)

    return max_length - 1 


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(longestSubarray(nums))  
