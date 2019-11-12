# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1