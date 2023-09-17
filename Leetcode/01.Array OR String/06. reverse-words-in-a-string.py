class Solution:
    def reverseWords(self, s: str) -> str:
        string = ""
        reverse = []
        temp = ""
        
        for i in s:
            if i!=" ":
                temp += i
            elif temp != "":
                reverse.append(temp)
                temp = ""
        if temp != "":
            reverse.append(temp)


        for i in reverse[::-1]:
            string += i
            string += " "

        return string[:-1]

solution= Solution()
result= solution.reverseWords('The name is Aadish')
print(result)
