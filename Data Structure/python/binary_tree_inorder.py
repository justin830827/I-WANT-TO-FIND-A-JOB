# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
        Input: [1,null,2,3]
        Output: [1,3,2]
    """
    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        """
        Recursion solution with helper

        Args:
            root: Given an root of a binary tree

        Returns:
            a list of inorder traversal of tree

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        def helper(x):
            if not x:
                return
            
            helper(x.left)
            res.append(x.val)
            helper(x.right)
        helper(root)
        return res
    
    def inorderTraversalIteration(self, root: TreeNode) -> List[int]:
        """
        Iteration solution with stack

        Args:
            root: Given an root of a binary tree

        Returns:
            a list of inorder traversal of tree

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cur = root
        res, stack = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    
    def inorderMorrisTraversal(self, root: TreeNode) -> List[int]:
        """
        Morris inorder traversal solution

        Args:
            root: Given an root of a binary tree

        Returns:
            a list of inorder traversal of tree

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        res = []
        cur = root
        while cur:
            if cur.left:
                rightmost = cur.left
                # Find the rightmost node
                while rightmost.right:
                    rightmost = rightmost.right
                tmp = cur
                rightmost.right = tmp
                cur = cur.left
                tmp.left = None
            else:
                res.append(cur.val)
                cur = cur.right
        return res
    
