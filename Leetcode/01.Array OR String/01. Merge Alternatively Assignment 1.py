class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #print(len(word1))
        #print(len(word2))
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

class Reverse(Solution):
    def reverseMerge(self, merged: str) -> str:
        
        # Converted the string to swap
        string = list(merged)
        length = len(string)
        
        #For loop to swap characters from the beginning and end
        for i in range(length // 2):
            string[i], string[length - i - 1] = string[length - i - 1], string[i]
        
        # Join the reversed characters back into a string
        reversed_result = ''.join(string)
        return reversed_result

# Create an instance of the Solution class
solution = Reverse()


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
merged_result = solution.mergeAlternately(word1, word2)


reversed_result = solution.reverseMerge(merged_result)


#print("Merged Result:", merged_result)
#print("Reversed Result:", reversed_result)
