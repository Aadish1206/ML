def findMaxAverage(nums, k):
    current_sum = sum(nums[:k])
    #print(current_sum)
    max_average = current_sum / k
    #print(max_average)

    i = k 
    
    while i < len(nums):
        current_sum += nums[i] - nums[i - k]
        #print(current_sum)

        if current_sum / k > max_average:
            max_average = current_sum / k
            #print(max_average)

        i += 1  
    return max_average


nums = [1, 12, -5, -6, 50, 3]
k = 4
result = findMaxAverage(nums, k)
print(result)  
