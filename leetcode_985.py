class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        answer = []
        for i in nums:
            if i%2==0:
                even_sum+=i
        for i in queries:
            val_i = i[0]
            index_i = i[1]
            new_nums_i = nums[index_i] + val_i
            if nums[index_i]%2==0 and new_nums_i%2==1:
                even_sum -= nums[index_i]
            elif nums[index_i]%2==0 and new_nums_i%2==0:
                even_sum += new_nums_i - nums[index_i]
            elif nums[index_i]%2==1 and new_nums_i%2==0:
                even_sum += new_nums_i
            nums[index_i] = nums[index_i] + val_i
            answer.append(even_sum)
        return answer

#O(n) solution
#https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/