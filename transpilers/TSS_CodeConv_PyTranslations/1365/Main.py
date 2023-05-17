class Solution:
    def __init__(self):
        #instance fields found by Java to Python Converter:
        Solution.memo = None
        self.trees = HashSet()
        self._result = 0
        self._cache = None

        Solution.memo = []
        Solution.memo.add(0)
        Solution.memo.add(1)
    def fib(self, N):
        if N < Solution.memo.size():
            return Solution.memo.get(N)
        for i in range(Solution.memo.size(), N + 1):
            Solution.memo.add(Solution.memo.get(i - 1) + Solution.memo.get(i - 2))
        return Solution.memo.get(N)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        N = 2
        out = sObj.fib(N)
        print(out)
