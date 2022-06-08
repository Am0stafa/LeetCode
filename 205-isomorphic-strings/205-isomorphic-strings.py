class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map ={}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if t[i] in map.values() and s[i] not in map.keys():
                return False
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            else:
                map[s[i]] = t[i]
        return True