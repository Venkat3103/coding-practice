class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}

        for i in range(0,len(nums)):
            val = nums[i]
            to_search = target-val
            if to_search in nums_dict:
                ind = nums_dict[to_search]
                return [i,ind]
            if val not in nums_dict:
                nums_dict[val] = i

#https://leetcode.com/problems/two-sum/description/