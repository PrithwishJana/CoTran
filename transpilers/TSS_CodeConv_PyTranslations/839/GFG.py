class GFG:
    @staticmethod
    def getLeftMostZero(zero):
        if zero.isEmpty():
            return - 1
        zero.remove()
        return 0
    @staticmethod
    def getLeftMostOne(one):
        if one.isEmpty():
            return - 1
        one.remove()
        return 1
    @staticmethod
    def getLeftMostElement(zero, one):
        if zero.isEmpty() and one.isEmpty():
            return - 1
        elif zero.isEmpty():
            one.remove()
            return 1
        elif one.isEmpty():
            zero.remove()
            return 0
        res = 0 if (zero.peek() < one.peek()) else 1
        if res == 0:
            zero.remove()
        else:
            one.remove()
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def performQueries(arr, n, queries, q):
        zero = LinkedList()
        one = LinkedList()
        for i in range(0, n):
            if arr [i] == 0:
                zero.add(i)
            else:
                one.add(i)
        for i in range(0, q):
            type = queries [i]
            if type == 1:
                print(GFG.getLeftMostZero(zero))
            elif type == 2:
                print(GFG.getLeftMostOne(one))
            elif type == 3:
                print(GFG.getLeftMostElement(zero, one))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 0, 1, 1, 1]
        n = len(arr)
        queries = [1, 3, 1]
        q = len(queries)
        GFG.performQueries(arr, n, queries, q)
