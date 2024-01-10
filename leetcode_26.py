class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uc = 1
        for i in nums:
            if i>nums[uc-1]:
                nums[uc] = i
                uc+=1
        return uc

#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/