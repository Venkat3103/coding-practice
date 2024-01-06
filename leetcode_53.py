class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

    #check the last element in the list, if it is negative, add the number to the list. if it is postive, add the number plus the last element into the list. If the list is empty, add the number to the list.
        last_ele = None
        maxSum = nums[0]
        for i in nums:
            if last_ele==None or last_ele<0:
                last_ele = i
            else:
                last_ele = i+last_ele
            if last_ele>maxSum:
                maxSum = last_ele
        return maxSum

#https://leetcode.com/problems/maximum-subarray/description/
#Beats 98% users - Runtime