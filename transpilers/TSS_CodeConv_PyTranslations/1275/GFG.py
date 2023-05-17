class GFG:
    class Node:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.data = 0
            self.next = None
            self.prev = None
            self.left = None
            self.right = None

    class INT:
        def __init__(self, a):
            #instance fields found by Java to Python Converter:
            self.a = 0

            self.a = a
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def newNode(data):
        temp = Node()
        temp.data = data
        temp.left = temp.right = None
        return temp
    @staticmethod
    def printInorder(node):
        if node is None:
            return
        GFG.printInorder(node.left)
        print("{0:d} ".format(node.data), end = '')
        GFG.printInorder(node.right)
    @staticmethod
    def conBinaryTreeUtil(pre, preM, preIndex, l, h, size):
        if preIndex.a >= size or l > h:
            return None
        root = GFG.newNode(pre [preIndex.a])
        ++ (preIndex.a)
        if l == h:
            return root
        i = 0
        for i in range(l, h + 1):
            if pre [preIndex.a] == preM [i]:
                break
        if i <= h:
            root.left = GFG.conBinaryTreeUtil(pre, preM, preIndex, i, h, size)
            root.right = GFG.conBinaryTreeUtil(pre, preM, preIndex, l + 1, i - 1, size)
        return root
    @staticmethod
    def conBinaryTree(root, pre, preMirror, size):
        preIndex = INT(0)
        preMIndex = 0
        root = GFG.conBinaryTreeUtil(pre, preMirror, preIndex, 0, size - 1, size)
        GFG.printInorder(root)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        preOrder = [1, 2, 4, 5, 3, 6, 7]
        preOrderMirror = [1, 3, 7, 6, 2, 5, 4]
        size = len(preOrder)
        root = Node()
        GFG.conBinaryTree(root, preOrder, preOrderMirror, size)
