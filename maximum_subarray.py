
# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# naive approach: go through the entire array, get the sum from the first item to 
# the next item, then first item to the next next time and continue. Then go 
# though the entire array again starting the second item to the next item. Until
# the end, after getting all the sum, pick the max sum. runtime is O(n^2) because
# we have nested loop to compute the sum

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    if not nums:
        return 0

    cur_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(cur_sum, max_sum)

    return max_sum