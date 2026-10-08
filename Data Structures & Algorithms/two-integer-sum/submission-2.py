class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in count:
                return [count[dif], i]
            count[nums[i]] = i