# Given two strings s and t , write a function to determine if t is an anagram of s.


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # simple way using sort
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

        #using hashmap
        hash_table = {}
    
        for i in s:
            hash_table[i] = hash_table.get(i, 0) + 1
                
        for j in t:
            if j not in hash_table:
                return False
            
            hash_table[j] -= 1
            if hash_table[j] == 0:
                del hash_table[j]
                
        return len(hash_table) == 0