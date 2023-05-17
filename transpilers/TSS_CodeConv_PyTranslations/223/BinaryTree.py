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
#ORIGINAL LINE: public Node(int data)
    def __init__(self, data):
        self._initialize_instance_fields()

        self.data = data
        self.left = self.right = None
class BinaryTree:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.root = None

    def printSpecificLevelOrderUtil(self, root, s):
        if root is None:
            return
        q = LinkedList()
        q.add(root.left)
        q.add(root.right)
        first = None
        second = None
        while not q.isEmpty():
            first = q.peek()
            q.poll()
            second = q.peek()
            q.poll()
            s.push(second.left)
            s.push(first.right)
            s.push(second.right)
            s.push(first.left)
            if first.left.left is not None:
                q.add(first.right)
                q.add(second.left)
                q.add(first.left)
                q.add(second.right)
    def printSpecificLevelOrder(self, root):
        s = Stack()
        s.push(root)
        if root.left is not None:
            s.push(root.right)
            s.push(root.left)
        if root.left.left is not None:
            self.printSpecificLevelOrderUtil(root, s)
        while not s.empty():
            print(s.peek().data + " ", end = '')
            s.pop()
    @staticmethod
    def main(args):
        tree = BinaryTree()
        tree.root = Node(1)
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        print("Specific Level Order Traversal of Binary Tree is")
        tree.printSpecificLevelOrder(tree.root)
