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

        # bruteForce method, runtime is O(n^2) because of nested loops
        for i in range(len(nums)):        
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

        # Linear runtime solution using hashmap
       
        
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                if hash_map[complement] != i:
                    return [i, hash_map[complement]]
        return []




                