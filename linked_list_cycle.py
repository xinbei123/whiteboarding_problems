# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which 
# represents the position (0-indexed) in the linked list where tail connects to. 
# If pos is -1, then there is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        hash_map = {}
        
        while head:
            if head in hash_map:
                return True
            else:
                hash_map[head] = hash_map.get(head,0) + 1
                
            head = head.next

        return False