def findDisjoint(nums1, nums2):
    unique_nums1 = list(set(nums1) - set(nums2))  
    #print(unique_nums1)
    unique_nums2 = list(set(nums2) - set(nums1))  
    #print(unique_nums2)

    return [unique_nums1, unique_nums2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result1 = findDisjoint(nums1, nums2)
print(result1)  

nums3 = [1, 2, 3, 3]
nums4 = [1, 1, 2, 2]
result2 = findDisjoint(nums3, nums4)
print(result2)  
