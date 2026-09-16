class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = 0
        res = []
        for i in range(len(arr) - 1):
            res.append(max(arr[i + 1:]))
        res.append(-1)
        return res