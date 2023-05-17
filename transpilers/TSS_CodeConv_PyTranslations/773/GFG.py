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
        new_node.next = (head_ref)
        (head_ref) = new_node
        return head_ref
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if math.fmod(n, 2) == 0 or math.fmod(n, 3) == 0:
            return False
        i = 5
        while i * i <= n:
            if math.fmod(n, i) == 0 or math.fmod(n, (i + 2)) == 0:
                return False
            i = i + 6
        return True
    @staticmethod
    def deleteNonPrimeNodes(head_ref):
        ptr = head_ref
        while ptr is not None and not GFG.isPrime(ptr.data):
            temp = ptr
            ptr = ptr.next
        head_ref = ptr
        if ptr is None:
            return None
        curr = ptr.next
        while curr is not None:
            if not GFG.isPrime(curr.data):
                ptr.next = curr.next
                curr = ptr.next
            else:
                ptr = curr
                curr = curr.next
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
        head = GFG.push(head, 17)
        head = GFG.push(head, 7)
        head = GFG.push(head, 6)
        head = GFG.push(head, 16)
        head = GFG.push(head, 15)
        print("Original List: ", end = '')
        GFG.printList(head)
        head = GFG.deleteNonPrimeNodes(head)
        print("\nModified List: ", end = '')
        GFG.printList(head)
