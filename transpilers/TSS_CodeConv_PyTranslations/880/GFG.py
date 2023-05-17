class GFG:
    @staticmethod
    def maximumXor(arr, n):
        sForward = Stack()
        sBackward = Stack()
        ans = - 1
        for i in range(0, n):
            while (not sForward.isEmpty()) and arr [i] < arr [sForward.peek()]:
                ans = max(ans, arr [i] ^ arr [sForward.peek()])
                sForward.pop()
            sForward.add(i)
            while (not sBackward.isEmpty()) and arr [n - i - 1] < arr [sBackward.peek()]:
                ans = max(ans, arr [n - i - 1] ^ arr [sBackward.peek()])
                sBackward.pop()
            sBackward.add(n - i - 1)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [8, 1, 2]
        n = len(arr)
        print(GFG.maximumXor(arr, n), end = '')
