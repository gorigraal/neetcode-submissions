class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = []
        r = len(s) - 1
        while r >= 0:
            res.append(s[r])
            r -= 1
        for i in range(len(s)):
            s[i] = res[i]