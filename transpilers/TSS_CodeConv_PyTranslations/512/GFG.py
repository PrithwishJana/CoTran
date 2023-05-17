import math

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
    def push(head_ref, new_data):
        new_node = Node()
        new_node.data = new_data
        new_node.prev = None
        new_node.next = (head_ref)
        if (head_ref) is not None:
            (head_ref).prev = new_node
        (head_ref) = new_node
        return head_ref
    @staticmethod
    def makeOddNode(head_ref, A, n):
        ptr = head_ref
        next = None
        i = 0
        while ptr is not None:
            next = ptr.next
            if math.fmod(ptr.data, 2) == 0:
                ptr.data = A [i]
                i += 1
            ptr = next
        return head_ref
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printList(head):
        while head is not None:
            print(str(head.data) + " ", end = '')
            head = head.next
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        head = None
        Arr = [3, 5, 23, 17, 1]
        head = GFG.push(head, 4)
        head = GFG.push(head, 7)
        head = GFG.push(head, 8)
        head = GFG.push(head, 9)
        head = GFG.push(head, 6)
        n = len(Arr)
        print("Original List: ", end = '')
        GFG.printList(head)
        print()
        head = GFG.makeOddNode(head, Arr, n)
        print("New odd List: ", end = '')
        GFG.printList(head)
