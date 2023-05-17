class Solution:
    def xorQueries(self, arr, queries):
        res = [0 for _ in range(len(queries))]
        q = None
        i = 1
        while i < len(arr):
            arr [i] ^= arr [i - 1]
            i += 1
        i = 0
        while i < len(queries):
            q = queries [i]
            res [i] = arr [q [0] - 1] ^ arr [q [1]] if q [0] > 0 else arr [q [1]]
            i += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        arr = [1, 3, 4, 8]
        queries = [[ 0, 1 ], [ 1, 2 ], [ 0, 3 ], [ 3, 3 ]]
        out = sObj.xorQueries(arr, queries)
        print(Arrays.toString(out))
