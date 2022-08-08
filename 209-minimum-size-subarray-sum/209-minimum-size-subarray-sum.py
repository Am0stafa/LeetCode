class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,total = 0,0
        output = float('inf')
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                output = min(r-l +1 , output)
                total -=nums[l]
                l+=1
        return 0 if output == float('inf') else output
            