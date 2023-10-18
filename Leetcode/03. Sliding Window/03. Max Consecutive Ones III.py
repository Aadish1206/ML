def longestOnes(nums, k):
    max_length = 0
    left = 0  # Left pointer of the sliding window
    count = 0  # Count of 0's in the window

    for right in range(len(nums)):
        if nums[right] == 0:
            count += 1

        while count > k:
            if nums[left] == 0:
                count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k1 = 2
print(longestOnes(nums1, k1))  


nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k2 = 3
print(longestOnes(nums2, k2))  
