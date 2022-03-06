class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        currentSum = 0
        
        for n in nums:
            if currentSum<0:
                currentSum =0
            currentSum += n
            maxSoFar = max(maxSoFar,currentSum)
        return maxSoFar