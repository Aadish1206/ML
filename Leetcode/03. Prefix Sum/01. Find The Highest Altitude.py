def findHighestAltitude(gain):
    highest = 0
    current = 0

    for i in range(len(gain)):
        current += gain[i] 
        highest = max(highest, current)

    return highest


gain1 = [-5, 1, 5, 0, -7]
print(findHighestAltitude(gain1))  


gain2 = [-4, -3, -2, -1, 4]
print(findHighestAltitude(gain2))  
