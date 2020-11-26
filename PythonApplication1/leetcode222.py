#222. 完全二叉树的节点个数
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global num
        num=0
        def fun(root):
            global num
            if(not root):
                return 
            num+=1
            fun(root.left)
            fun(root.right)
        fun(root)
        return num