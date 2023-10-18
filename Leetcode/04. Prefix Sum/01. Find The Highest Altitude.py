def findHighestAltitude(gain):
    highest = 0
    current = 0

    for i in range(len(gain)):
        current += gain[i] 
        #print(current)
        highest = max(highest, current)
        #print(highest)

    return highest


gain1 = [-5, 1, 5, 0, -7]
print(findHighestAltitude(gain1))  


gain2 = [-4, -3, -2, -1, 4]
print(findHighestAltitude(gain2))  
