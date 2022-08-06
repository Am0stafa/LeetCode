class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentWord = ""
        res = 0
        l,r = 0, 1
        if len(s)==1:
            return 1
        while r < len(s):
            if currentWord == "":
                currentWord+=s[l]
            if not s[r] in currentWord:
                currentWord+=s[r]      
                res = max(len(currentWord),res)
            else:
                res = max(len(currentWord),res)
                currentWord = ""
                l+=1
                r = l
            r+=1    
        return res