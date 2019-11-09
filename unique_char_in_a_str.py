# Given a string, find the first non-repeating character in it and return it's 
# index. If it doesn't exist, return -1.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for i in range(len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1

        for i, char in enumerate(s):
            if hash_map[char] == 1:
                return i
        return -1