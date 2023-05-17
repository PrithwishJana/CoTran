class Linked_list_2D_Matrix:
    class Node:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.data = 0
            self.right = None
            self.down = None

    @staticmethod
    def construct(arr, i, j, m, n):
        if i > n - 1 or j > m - 1:
            return None
        temp = Node()
        temp.data = arr [i][j]
        temp.right = Linked_list_2D_Matrix.construct(arr, i, j + 1, m, n)
        temp.down = Linked_list_2D_Matrix.construct(arr, i + 1, j, m, n)
        return temp
    @staticmethod
    def display(head):
        Rp = None
        Dp = head
        while Dp is not None:
            Rp = Dp
            while Rp is not None:
                print(str(Rp.data) + " ", end = '')
                Rp = Rp.right
            print()
            Dp = Dp.down
    @staticmethod
    def main(args):
        arr = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
        m = 3
        n = 3
        head = Linked_list_2D_Matrix.construct(arr, 0, 0, m, n)
        Linked_list_2D_Matrix.display(head)
