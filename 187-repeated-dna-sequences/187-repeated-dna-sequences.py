class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        output = []
        rep = set()

        for i in range(len(s)-9):

                if s[i:i+10] in rep and not s[i:i+10] in output :
                    output.append(s[i:i+10])
                    rep.remove(s[i:i+10])
                else:
                    rep.add(s[i:i+10])

        
        return output
        