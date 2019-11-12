# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which 
# represents the position (0-indexed) in the linked list where tail connects to. 
# If pos is -1, then there is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# hashmap solution, O(n) time complexity vs O(n) space complexity
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

# two pointer solution, O(n) time complexity vs O(1) space complexity
 def hasCycle(self, head):
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                return True
            
            slow = slow.next
            fast = fast.next.next
        
        return False


        