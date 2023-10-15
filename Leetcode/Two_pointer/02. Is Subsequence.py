def isSubsequence(s, t):
    first = 0 #First create two pointers
    second = 0
    
    #Create a string compare to compare strings
    while first < len(s) and second < len(t):
        if s[first] == t[second]:
            first += 1
            #print(first)
        second += 1
        #print(second)
        
    if first == len(s):
        return True
    else:
        return False

s1 = "abc"
t1 = "aadbishcwar"
print(isSubsequence(s1, t1))  

s2 = "cad"
t2 = "aadishwar"
print(isSubsequence(s2, t2))  
