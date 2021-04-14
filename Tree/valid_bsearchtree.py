# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Need to make sure ALL elements in left subtree are less than highest parent node and all elements in
    right subtree are greater than greatest parent node. To do this, pass minVal and maxVal seen so far
    during the recursion
        5
      /  \
     1    6
         / \
        4   7
    '''
    def isValidBST(self, root: TreeNode) -> bool:
        
        def _isValidBST(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val <= minVal or root.val >= maxVal:
                return False
            
            return _isValidBST(root.left, minVal, root.val) and _isValidBST(root.right, root.val, maxVal)
            
        
        return _isValidBST(root, float('-inf'), float('inf'))
    
            