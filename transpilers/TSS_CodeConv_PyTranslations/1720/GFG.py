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
#ORIGINAL LINE: Node(int x)
        def __init__(self, x):
            self._initialize_instance_fields()

            self.data = x
            self.next = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printList(head):
        if head is None:
            return
        temp = head
        loop_condition = True
        while loop_condition:
            print(str(temp.data) + "->", end = '')
            temp = temp.next
            loop_condition = temp is not head
        print(head.data)
    @staticmethod
    def deleteK(head_ref, k):
        head = head_ref
        if head is None:
            return None
        curr = head
        prev = None
        while True:
            if curr.next is head and curr is head:
                break
            GFG.printList(head)
            for i in range(0, k):
                prev = curr
                curr = curr.next
            if curr is head:
                prev = head
                while prev.next is not head:
                    prev = prev.next
                head = curr.next
                prev.next = head
                head_ref = head
            elif curr.next is head:
                prev.next = head
            else:
                prev.next = curr.next
        return head
    @staticmethod
    def insertNode(head_ref, x):
        head = head_ref
        temp = Node(x)
        if head is None:
            temp.next = temp
            head_ref = temp
            return head_ref
        else:
            temp1 = head
            while temp1.next is not head:
                temp1 = temp1.next
            temp1.next = temp
            temp.next = head
        return head
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        head = None
        head = GFG.insertNode(head, 1)
        head = GFG.insertNode(head, 2)
        head = GFG.insertNode(head, 3)
        head = GFG.insertNode(head, 4)
        head = GFG.insertNode(head, 5)
        head = GFG.insertNode(head, 6)
        head = GFG.insertNode(head, 7)
        head = GFG.insertNode(head, 8)
        head = GFG.insertNode(head, 9)
        k = 4
        head = GFG.deleteK(head, k)
