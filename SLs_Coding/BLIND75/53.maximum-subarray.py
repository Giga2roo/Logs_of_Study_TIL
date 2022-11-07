#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            
            # Iterate fro the middle to the beginning.
            for i in range(mid -1, left -1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
                
            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right +1 ):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
                
            # The best_combined_sum uses the middle element and
            # The best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            
            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            
            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for any array - so just call it using the entire input!
        
        return findBestSubarray(nums, 0, len(nums) - 1)
            
            
        
# @lc code=end


'''
<First solution - Time Leamit Exceeded>

        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
                
        return max_subarray




<Second solution>
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
                # if current_subarray is negative, throw it away. Otherwise, keep adding to it.
                current_subarray = max(num, current_subarray + num)
                max_subarray = max(max_subarray, current_subarray)
                
        return max_subarray
        
Accepted
209/209 cases passed (2205 ms)
Your runtime beats 10.24 % of python3 submissions
Your memory usage beats 78.23 % of python3 submissions (27.9 MB)



<Third solution>

        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            
            # Iterate fro the middle to the beginning.
            for i in range(mid -1, left -1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
                
            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right +1 ):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
                
            # The best_combined_sum uses the middle element and
            # The best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            
            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            
            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for any array - so just call it using the entire input!
        
        return findBestSubarray(nums, 0, len(nums) - 1)

Accepted
209/209 cases passed (7160 ms)
Your runtime beats 5 % of python3 submissions
Your memory usage beats 78.23 % of python3 submissions (27.9 MB)            

'''


