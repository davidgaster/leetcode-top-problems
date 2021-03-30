# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class TreeNode:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def findLeaves(self, root) -> List[List[int]]:
        
        '''
        Naive: Use a while loop and recursively prune the tree's leaves while the
        entire tree still exists. Pass a parent node during the recursion which once you
        hit a leaf node, you delete that node from the parent.
        
        Tree's height
             1
            / \
           2   3
        num of nodes at level h = 2^h
        height of 4 --> 16
        total = 2 + 4 + 8 + 16 = N
        Runtime = O(nlogn)
        
        Optimization: O(n) complexity
        Get the height of every node in the traversal, then add it to that position
        int the output list
        []
        '''
        def dfs(node, parent, leaves):
            if not node:
                return
            
            if not node.right and not node.left:
                leaves.append(node.val)
                if parent.left == node: 
                    parent.left = None
                else:
                    parent.right = None
            
            if node.left:
                dfs(node.left, node, leaves)
            if node.right:
                dfs(node.right, node, leaves)
        
        if not root: return []
        ans = []
        while root.left or root.right:
            leaves = []
            dfs(root, None, leaves)
            ans.append(leaves)
        
        ans.append([root.val])
        
        return ans
    
        
def main():
    t1 = TreeNode(TreeNode(TreeNode(val=4), TreeNode(val=5), 2), TreeNode(val=3), val=1)
    got = Solution().findLeaves(t1)
    ans = [[4,5,3],[2],[1]]
    print(f'{got} ==  {ans}')
    assert got == ans

if __name__ == "__main__":
    main()