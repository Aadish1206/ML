def longestSubarray(nums):
    max_length = 0
    left, right = 0, 0  

    while right < len(nums):
        if nums[right] == 0:
            left = right  

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length - 1 


nums1 = [1, 1, 0, 1]
print(longestSubarray(nums1)) 


nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(longestSubarray(nums2)) 
