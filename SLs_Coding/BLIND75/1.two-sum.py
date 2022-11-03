#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# @lc code=end


```
LeetCode 
- [BLIND75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
- [01 Two Sum](https://leetcode.com/problems/two-sum/)

input 
- array of integers as `nums`
- an integer `target`

return
- `two numbers` such that they add up to `target`

constraints
- each input would have exactly one solution
- not use the same element twice
```