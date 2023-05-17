class GFG:
    class Node:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.data = 0
            self.next = None
            self.prev = None
            self.left = None
            self.right = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Node(int data)
        def __init__(self, data):
            self._initialize_instance_fields()

            self.data = data
            self.next = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printList(node):
        while node is not None:
            print(str(node.data) + " -> ", end = '')
            node = node.next
        print("NULL")
    @staticmethod
    def cntNodes(node):
        if node is None:
            return 0
        return (1 + GFG.cntNodes(node.next))
    @staticmethod
    def updateList(head, m):
        cnt = GFG.cntNodes(head)
        if cnt != m and m < cnt:
            skip = cnt - m
            prev = None
            curr = head
            while skip > 0:
                prev = curr
                curr = curr.next
                skip -= 1
            prev.next = None
            tempHead = head
            head = curr
            while curr.next is not None:
                curr = curr.next
            curr.next = tempHead
        GFG.printList(head)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        head = Node(4)
        head.next = Node(5)
        head.next.next = Node(6)
        head.next.next.next = Node(1)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(3)
        m = 3
        GFG.updateList(head, m)
