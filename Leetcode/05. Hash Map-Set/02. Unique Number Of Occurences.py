def uniqueOccurrences(arr):
    
    num_counts = {}
    for num in arr:
        if num in num_counts:
            num_counts[num] += 1
            #print(num_counts)
        else:
            num_counts[num] = 1
            #print(num_counts)

    
    counts = set(num_counts.values())
    #print(counts)
    return len(counts) == len(num_counts)
    
print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
