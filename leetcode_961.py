class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        element_count = {}
        for i in nums:
            if i not in element_count.keys():
                element_count[i] = 1
            else:
                return i

#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/