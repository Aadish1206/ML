from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_element = 0
        #print(max_element)
        
        for i in range(len(candies)):
            if candies[i] > max_element:
                max_element = candies[i]
                
        #print(max_element)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            #print(candies[i])
            
        result = [] 

        for i in range(len(candies)):
            if candies[i] > max_element:
                result.append(True)
            else:
                result.append(False)

        return result  
solution = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = solution.kidsWithCandies(candies, extraCandies)
#print(result)
