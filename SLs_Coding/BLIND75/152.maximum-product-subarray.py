#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            
            max_so_far = temp_max
            
            result = max(max_so_far, result)
        
        return result
        
# @lc code=end


'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        result = nums[0]
        
        for i in range(len(nums)):
            accumulator = 1
            for j in range(i, len(nums)):
                accumulator *= nums[j]
                result = max(result, accumulator)
        
        return result
        
        
Time Limit Exceeded
186/188 cases passed (N/A)        

==================================================================



'''

