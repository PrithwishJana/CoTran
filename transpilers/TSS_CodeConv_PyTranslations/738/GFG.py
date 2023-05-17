class Node:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.type = None
        self.isOption = False
        self.child = None
        self.id = 0
        self.depth = 0
        self.contents = None
        self.children = None
        self.data = 0
        self.left = None
        self.right = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Node(int data)
    def __init__(self, data):
        self._initialize_instance_fields()

        self.data = data
        self.left = self.right = None
class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def insert(root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = GFG.insert(root.left, data)
        if data > root.data:
            root.right = GFG.insert(root.right, data)
        return root
    @staticmethod
    def inOrder(root):
        if root is None:
            return
        GFG.inOrder(root.left)
        print(str(root.data) + " ", end = '')
        GFG.inOrder(root.right)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 2, 5, 4, 4]
        n = len(arr)
        root = None
        for i in range(0, n):
            root = GFG.insert(root, arr [i])
        GFG.inOrder(root)
