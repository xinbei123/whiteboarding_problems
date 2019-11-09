# Given an integer array nums, find the contiguous subarray (containing at least 
# one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], nums[i]+current_sum)
            max_sum = max(max_sum, current_sum)