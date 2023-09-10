class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        
        merged = ""
        a = 0
        b = 0
        
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
