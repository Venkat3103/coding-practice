class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxval = 1
        minval = 1
        maxProd = max(nums)
        for i in nums:
            if i==0:
                maxval = 1
                minval = 1
            val1 = maxval*i
            val2 = minval*i
            maxval = max(val1,val2,i)
            minval = min(val1,val2,i)
            maxProd = max(maxProd,val1,val2)
        return maxProd

#https://leetcode.com/problems/maximum-product-subarray/description/
