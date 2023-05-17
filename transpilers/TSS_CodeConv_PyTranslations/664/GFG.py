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
        temp = Node()
        temp.data = data
        temp.left = temp.right = None
        return temp
    @staticmethod
    def getDeepestRightLeafNode(root):
        if root is None:
            return None
        q = LinkedList()
        q.add(root)
        result = None
        while not q.isEmpty():
            temp = q.peek()
            q.poll()
            if temp.left is not None:
                q.add(temp.left)
            if temp.right is not None:
                q.add(temp.right)
                if temp.right.left is None and temp.right.right is None:
                    result = temp.right
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        root = GFG.newNode(1)
        root.left = GFG.newNode(2)
        root.right = GFG.newNode(3)
        root.left.right = GFG.newNode(4)
        root.right.left = GFG.newNode(5)
        root.right.right = GFG.newNode(6)
        root.right.left.right = GFG.newNode(7)
        root.right.right.right = GFG.newNode(8)
        root.right.left.right.left = GFG.newNode(9)
        root.right.right.right.right = GFG.newNode(10)
        result = GFG.getDeepestRightLeafNode(root)
        if result is not None:
            print("Deepest Right Leaf Node :: " + str(result.data))
        else:
            print("No result, right leaf not found\n")
