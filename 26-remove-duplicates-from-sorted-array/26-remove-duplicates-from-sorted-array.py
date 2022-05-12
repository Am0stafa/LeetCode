class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        m ={}
        for i in range(len(nums)):
            if not m.get(nums[i]):
                nums[unique] = nums[i]
                unique+=1
                m[nums[i]] = 1
        return unique
                
        