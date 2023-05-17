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
    def pathSum(self, root, sum):
        self._result = 0
        self._cache = {}
        self._cache[0] = 1
        self._pathSumHelper(root, sum, 0)
        return self._result
    def _pathSumHelper(self, root, target, soFar):
        if root is not None:
            complement = soFar + root.val - target
            if complement in self._cache.keys():
                self._result += self._cache[complement]
            self._cache[soFar + root.val] = self._cache.getOrDefault(soFar + root.val, 0) + 1
            self._pathSumHelper(root.left, target, soFar + root.val)
            self._pathSumHelper(root.right, target, soFar + root.val)
            self._cache[soFar + root.val] = self._cache[soFar + root.val] - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        tree = TreeNode(10)
        tree.left = TreeNode(5)
        tree.right = TreeNode(- 3)
        tree.left.left = TreeNode(3)
        tree.left.right = TreeNode(2)
        tree.right.right = TreeNode(11)
        tree.left.left.left = TreeNode(3)
        tree.left.left.right = TreeNode(- 2)
        tree.left.right.right = TreeNode(1)
        sum = 8
        out = sObj.pathSum(tree, sum)
        print(out)
