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
    def getNode(data):
        newNode = Node()
        newNode.data = data
        return newNode
    @staticmethod
    def insertEnd(head, new_node):
        if head is None:
            new_node.next = new_node.prev = new_node
            head = new_node
            return head
        last = (head).prev
        new_node.next = head
        (head).prev = new_node
        new_node.prev = last
        last.next = new_node
        return head
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def reverse(head):
        if head is None:
            return None
        new_head = None
        last = head.prev
        curr = last
        prev = None
        while curr.prev is not last:
            prev = curr.prev
            new_head = GFG.insertEnd(new_head, curr)
            curr = prev
        new_head = GFG.insertEnd(new_head, curr)
        return new_head
    @staticmethod
    def display(head):
        if head is None:
            return
        temp = head
        print("Forward direction: ", end = '')
        while temp.next is not head:
            print(str(temp.data) + " ", end = '')
            temp = temp.next
        print(str(temp.data) + " ", end = '')
        last = head.prev
        temp = last
        print("\nBackward direction: ", end = '')
        while temp.prev is not last:
            print(str(temp.data) + " ", end = '')
            temp = temp.prev
        print(str(temp.data) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        head = None
        head = GFG.insertEnd(head, GFG.getNode(1))
        head = GFG.insertEnd(head, GFG.getNode(2))
        head = GFG.insertEnd(head, GFG.getNode(3))
        head = GFG.insertEnd(head, GFG.getNode(4))
        head = GFG.insertEnd(head, GFG.getNode(5))
        print("Current list:\n", end = '')
        GFG.display(head)
        head = GFG.reverse(head)
        print("\n\nReversed list:\n", end = '')
        GFG.display(head)
