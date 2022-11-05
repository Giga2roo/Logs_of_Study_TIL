#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False
        
# @lc code=end


'''
Trial#1 - Failed
        nums_unique = set(nums)
        
        if len(nums) != len(set(nums)):
            return("true")
        else:
            return("false")

Trial#2 - Succeeded
return True if len(set(nums)) < len(nums) else False

70/70 cases passed (968 ms)
Your runtime beats 62.2 % of python3 submissions
Your memory usage beats 67.61 % of python3 submissions (26 MB)

Trial#3 - succeeded
        visited = set()
        for num in nums:
            if num in visited:
                return True
            else:
                visited.add(num)
        return False

70/70 cases passed (989 ms)
Your runtime beats 59.82 % of python3 submissions
Your memory usage beats 27.82 % of python3 submissions (26 MB)
'''

