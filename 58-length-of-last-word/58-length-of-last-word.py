class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        print(l)
        
        for i in range(len(l)-1,-1,-1):
            if len(l[i]) > 0:
                return len(l[i])
            
        return 0