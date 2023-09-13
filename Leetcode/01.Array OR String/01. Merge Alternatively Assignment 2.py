class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #print(len(word1))
        #print(len(word2))
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        #initialise the merge to blank and a and b to zero
        merged = ""
        a = 0
        b = 0
        
        #while a is less than length of word 1 and b is less than length of word word2
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

class SplitMerge(Solution):
    def splitMerge(self, word1: str, word2: str) -> str:
    
        #Split word1 into two parts
        mid = len(word1) // 2
        word1part1 = word1[:mid]
        word1part2 = word1[mid:]

        #Split word2 into two parts and reverse them
        mid = len(word2) // 2
        word2part1 = word2[:mid]
        word2part2 = word2[mid:]
        word2part1 = word2part1[::-1]
        word2part2 = word2part2[::-1]

        
        #print("Part 1 of Word 1:", word1part1)
        #print("Part 2 of Word 1:", word1part2)
        #print("Part 1 of Word 2 (reversed):", word2part1)
        #print("Part 2 of Word 2 (reversed):", word2part2)

        #Merge the two words alternatively
        merged_word1 = self.mergeAlternately(word1part1, word1part2)
        merged_word2 = self.mergeAlternately(word2part1, word2part2)

        
        #print("Merged Word 1:", merged_word1)
        #print("Merged Word 2:", merged_word2)

        # Merge the two merged words alternatively
        final_merged_result = self.mergeAlternately(merged_word1, merged_word2)

        #print("Final Merged Result:", final_merged_result)
        
        return final_merged_result


solution = SplitMerge()
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
result = solution.splitMerge(word1, word2)
