class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #print(len(word1))
        #print(len(word2))
        
        #if length of word1 is zero then return word 2 and if word 2 is zero return word 1
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        
        merged = ""
        a = 0
        b = 0
        
        #while the variable a and b are less than the lengths of their words they keep combining the letters
        while a < len(word1) and b < len(word2):
            merged += word1[a] + word2[b]
            
            a += 1
            b += 1
        
        
        while a < len(word1):
            merged += word1[a]
            a += 1
            
        while b < len(word2):
            merged += word2[b]
            b += 1
            
        return merged

solution = Solution()
result = solution.mergeAlternately("Aadish", "Ramesh")
#print(result)
