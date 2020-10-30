#求根到叶子节点数字之和

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #递归，叶子节点返回求和值，非叶子节点递归左右节点求出对应的值并加和，空节点返回0
        def fun(root,num):
            if(not root):
                return 0
            sum1=num*10+root.val
            if(not root.left and not root.right):
                return sum1
            else:
                return fun(root.left,sum1)+fun(root.right,sum1)
    
        return fun(root,0)