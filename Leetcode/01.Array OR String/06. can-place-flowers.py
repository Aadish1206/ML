from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    count += 1
            i += 1
        return count >= n
solution = Solution()

flowerbed = [1, 0, 0, 0, 1]
n = 2

result = solution.canPlaceFlowers(flowerbed, n)

if result:
    print("True")
else:
    print("False")
