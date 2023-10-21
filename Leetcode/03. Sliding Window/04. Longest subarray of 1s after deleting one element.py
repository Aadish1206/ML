def longestSubarray(nums):
    max_length = 0
    current = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
            #print(zero_count)

        while zero_count > 1:
            if nums[current] == 0:
                zero_count -= 1
                #print(zero_count)
            current += 1
            #print(current)

        max_length = max(max_length, right - current + 1)

    return max_length - 1 

nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(longestSubarray(nums)) 
