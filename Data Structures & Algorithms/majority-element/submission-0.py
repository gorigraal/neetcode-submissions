class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        res = maxi = 0
        for num in nums:
            my_dict[num] += 1 
            if maxi < my_dict[num]:
                res = num
                maxi = my_dict[num]
        return res