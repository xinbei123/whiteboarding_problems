# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        head = l3 = ListNode(0)
        temp = 0
        
        while l1 or l2 or temp:
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
                
            l3.val = temp % 10
            temp = temp // 10
            
            if l1 or l2 or temp:
                l3.next = ListNode(0)
                l3 = l3.next
                
        return head