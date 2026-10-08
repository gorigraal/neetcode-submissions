class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = [0] * len(nums)
        sufix = [0] * len(nums)
        n = len(nums)

        prefix[0] = sufix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = sufix[i] * prefix[i]
        return res  