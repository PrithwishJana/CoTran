class GFG:
    class Node:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.data = 0
            self.next = None
            self.prev = None
            self.left = None
            self.right = None

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def newNode(data):
        node = Node()
        node.data = data
        node.left = None
        node.right = None
        return node
    @staticmethod
    def inorder(root):
        if root is None:
            return
        GFG.inorder(root.left)
        print(str(root.data) + " ", end = '')
        GFG.inorder(root.right)
    @staticmethod
    def isIdentical(root1, root2):
        if root1 is None and root2 is None:
            return 1
        elif root1 is not None and root2 is None:
            return 0
        elif root1 is None and root2 is not None:
            return 0
        else:
            if root1.data == root2.data and GFG.isIdentical(root1.left, root2.left) == 1 and GFG.isIdentical(root1.right, root2.right) == 1:
                return 1
            else:
                return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        root1 = GFG.newNode(5)
        root2 = GFG.newNode(5)
        root1.left = GFG.newNode(3)
        root1.right = GFG.newNode(8)
        root1.left.left = GFG.newNode(2)
        root1.left.right = GFG.newNode(4)
        root2.left = GFG.newNode(3)
        root2.right = GFG.newNode(8)
        root2.left.left = GFG.newNode(2)
        root2.left.right = GFG.newNode(4)
        if GFG.isIdentical(root1, root2) == 1:
            print("Both BSTs are identical", end = '')
        else:
            print("BSTs are not identical", end = '')
