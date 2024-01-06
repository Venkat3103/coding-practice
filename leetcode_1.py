class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            search = target - nums[i]
            if search in nums:
                i2 = nums.index(search)
                if(i!=i2):
                    out = [i,i2]
                    return out
#https://leetcode.com/problems/two-sum/description/