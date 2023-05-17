class TreeNode:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.val = 0
        self.left = None
        self.right = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public TreeNode(int rootData)
    def __init__(self, rootData):
        self._initialize_instance_fields()

        self.val = rootData
        self.left = None
        self.right = None
class Solution:
    def isSubtree(self, s, t):
        tree1 = self.preorder(s, True)
        tree2 = self.preorder(t, True)
        return tree1.find(tree2) >= 0
    def preorder(self, t, left):
        if t is None:
            if left:
                return "lnull"
            else:
                return "rnull"
        return "#" + str(t.val) + " " + self.preorder(t.left, True) + " " + self.preorder(t.right, False)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        out = sObj.isSubtree(root, subRoot)
        print(out)
