# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two 
# nodes in a tree. This path may or may not pass through the root.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        self.longest = 0
        
        def depth(root):
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.longest = max(self.longest, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.longest
        