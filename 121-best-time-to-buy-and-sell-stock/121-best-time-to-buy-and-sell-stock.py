

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi =0
        min =99999
        prof = 0
        
        for x in prices:
            if(x>maxi):
                maxi = x
            if(x<min):
                min = x
            calc = maxi - min
            prof = max(calc, prof)
            maxi = 0
            
        return prof