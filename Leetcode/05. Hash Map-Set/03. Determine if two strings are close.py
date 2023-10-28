def areStringsClose(word1, word2):
    if len(word1) != len(word2):
        return False

    count1 = {}
    count2 = {}

    for char in word1:
        count1[char] = count1.get(char, 0) + 1
        #print(count1)

    for char in word2:
        count2[char] = count2.get(char, 0) + 1
        #print(count2)

    return sorted(count1.values()) == sorted(count2.values()) and set(word1) == set(word2)


word1_1 = "abc"
word2_1 = "bca"
word1_2 = "a"
word2_2 = "aa"
word1_3 = "aaabbbbccddeeeeefffff"
word2_3 = "aaaaabbcccdddeeeeffff"

print(areStringsClose(word1_1, word2_1))  
print(areStringsClose(word1_2, word2_2))  
print(areStringsClose(word1_3, word2_3))  
