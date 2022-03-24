class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev = -1
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > prev:
                res.append(prev)
                prev = arr[i]
            else:
                res.append(prev)
        res.reverse()
        return res


        