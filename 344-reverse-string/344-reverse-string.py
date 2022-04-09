class Solution:
    def reverseString(self, s: List[str]) -> None:
        for x in range(len(s) // 2):
            temp = s[len(s) - (x + 1)]
            s[len(s) - (x + 1)] = s[x]
            s[x] = temp


        return s
        