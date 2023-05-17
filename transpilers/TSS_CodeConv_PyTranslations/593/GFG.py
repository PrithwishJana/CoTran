class GFG:
    class node:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.data = 0
            self.next = None

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def add(data):
        newnode = node()
        newnode.data = data
        newnode.next = None
        return newnode
    @staticmethod
    def printArr(a, n):
        for i in range(0, n):
            print(str(a [i]) + " ", end = '')
    @staticmethod
    def findlength(head):
        curr = head
        cnt = 0
        while curr is not None:
            cnt += 1
            curr = curr.next
        return cnt
    @staticmethod
    def convertArr(head):
        len = GFG.findlength(head)
        arr = [0 for _ in range(len)]
        index = 0
        curr = head
        while curr is not None:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: arr [index ++] = curr.data;
            arr [index ] = curr.data
            index += 1
            curr = curr.next
        GFG.printArr(arr, len)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        head = node()
        head = GFG.add(1)
        head.next = GFG.add(2)
        head.next.next = GFG.add(3)
        head.next.next.next = GFG.add(4)
        head.next.next.next.next = GFG.add(5)
        GFG.convertArr(head)
