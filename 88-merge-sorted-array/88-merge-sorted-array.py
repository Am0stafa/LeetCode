class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = (m+n)-1
        headnum1 = m -1
        headnums2 = n -1
        
        #merge in reverse order
        while headnum1+1 > 0 and headnums2+1 > 0:
            if nums2[headnums2] > nums1[headnum1]:
                nums1[tail] = nums2[headnums2]
                nums2[headnums2] = 0
                headnums2-=1
            else:
                nums1[tail] = nums1[headnum1]
                headnum1-=1         
            tail-=1
            
            
            
            
        #fill nums1 incase of left overs
        while headnums2+1 > 0:
            nums1[tail] = nums2[headnums2]
            nums2[headnums2] =0
            headnums2-=1
            tail-=1
        