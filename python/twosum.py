class Solution:
    def twoSum(self, nums:int, target: int):
        for i,value in enumerate(nums):
            in_list = target-value
            if in_list in nums and nums.index(in_list)!=i:
                return list([i,nums.index(in_list)])