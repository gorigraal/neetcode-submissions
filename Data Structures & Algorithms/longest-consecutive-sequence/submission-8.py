class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            
            if num - 1 not in nums_set:
                curr = num
                cnt = 0
                while curr in nums_set:
                    curr += 1
                    cnt += 1
                res = max(res, cnt)

        return res
                