# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # bruteForce method
        # time complexity o(n^2), space complexity O(1)

        for i in range(0, len(nums)):        
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

        # hashtable method
        # time complexity O(n), space complexity O(n)
       
        hash_map = {}

        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                if hash_map[complement] != i:
                    return [i, hash_map[complement]]

        return []

        




                