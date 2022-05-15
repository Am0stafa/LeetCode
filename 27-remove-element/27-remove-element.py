class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        isuu = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[isuu] = nums[i]
                isuu+=1
            
        return isuu