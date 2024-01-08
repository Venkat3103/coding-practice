class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while numbers[left]+numbers[right]!=target:
            if numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        return [left+1,right+1]

#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/