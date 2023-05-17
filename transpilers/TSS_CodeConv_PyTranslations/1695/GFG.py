import math

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
#ORIGINAL LINE: Node(int key)
    def __init__(self, key):
        self._initialize_instance_fields()

        self.data = key
        self.left = self.right = None
class GFG:
    @staticmethod
    def evenOddLevelDifference(root):
        if root is None:
            return 0
        q = LinkedList()
        q.add(root)
        level = 0
        evenSum = 0
        oddSum = 0
        while q.size() != 0:
            size = q.size()
            level += 1
            while size > 0:
                temp = q.remove()
                if math.fmod(level, 2) == 0:
                    evenSum += temp.data
                else:
                    oddSum += temp.data
                if temp.left is not None:
                    q.add(temp.left)
                if temp.right is not None:
                    q.add(temp.right)
                size -= 1
        return (oddSum - evenSum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        root = Node(5)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(4)
        root.left.right.left = Node(3)
        root.right.right = Node(8)
        root.right.right.right = Node(9)
        root.right.right.left = Node(7)
        print("Difference between sums is " + str(GFG.evenOddLevelDifference(root)))
