class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in store:
            if num - 1 not in store:
                curr, cnt = num, 0
                while curr in store:
                    cnt += 1
                    curr += 1
                res = max(cnt, res)
        return res
        