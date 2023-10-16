def maxVowels(s, k):
    vowels = set("aeiou")
    maximum = 0
    current = 0

    for i in range(len(s)):
        if s[i] in vowels:
            current += 1
            #print(current)
        
        if i >= k:
            if s[i - k] in vowels:
                current -= 1
                #print(current)

        maximum = max(maximum, current)

    return maximum


s1 = "abciiidef"
k1 = 3
print(maxVowels(s1, k1))  

s2 = "aeiou"
k2 = 2
print(maxVowels(s2, k2))  
