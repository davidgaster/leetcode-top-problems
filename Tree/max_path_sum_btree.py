# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''
    Idea: Find the maximum path down left subtree and right subtree + node itself
    The parent node can only choose ONE of those as the max path, so it chooses
    the max(left, right) + itself.
    Return the max pathsum we find along the way of the whole tree.
    path_sum = {
         -10: sum of left + sum of right
    }
           -10
          /   \
         9     20
              /  \
             15   7
    
    -10
    leftMax 9
    rightMax 35
    
    20
    leftMax 15
    rightMax 7
    
    '''
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        def dfs(root):
            nonlocal ans
            
            if not root:
                return 0
            
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            maxPath = left + right + root.val
            ans = max(ans, maxPath)
            return root.val + max(left, right)
            
        ans = root.val
        dfs(root)
        return ans