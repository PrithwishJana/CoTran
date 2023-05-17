class Solution:
    class INT:
        def __init__(self, d):
            #instance fields found by Java to Python Converter:
            self.data = 0

            self.data = d
    @staticmethod
    def findPostOrderUtil(pre, n, minval, maxval, preIndex):
        if preIndex.data == n:
            return
        if pre [preIndex.data] < minval or pre [preIndex.data] > maxval:
            return
        val = pre [preIndex.data]
        preIndex.data += 1
        Solution.findPostOrderUtil(pre, n, minval, val, preIndex)
        Solution.findPostOrderUtil(pre, n, val, maxval, preIndex)
        print(str(val) + " ", end = '')
    @staticmethod
    def findPostOrder(pre, n):
        preIndex = INT(0)
        Solution.findPostOrderUtil(pre, n, Integer.MIN_VALUE, Integer.MAX_VALUE, preIndex)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        pre = [40, 30, 35, 80, 100]
        n = len(pre)
        Solution.findPostOrder(pre, n)
