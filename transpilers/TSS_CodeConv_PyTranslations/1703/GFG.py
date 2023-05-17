class GFG:
    @staticmethod
    def coordinateCompression(arr, n):
        s = HashSet()
        for i in range(0, n):
            s.add(arr [i])
        index = 0
        mp = {}
        for itr in s:
            index += 1
            mp[itr] = index
        for i in range(0, n):
            arr [i] = mp[arr [i]]
    @staticmethod
    def query(BIT, index, n):
        ans = 0
        while index > 0:
            ans = max(ans, BIT [index])
            index -= index & (- index)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def update(BIT, index, n):
        x = GFG.query(BIT, index - 1, n)
        value = x + 1
        while index <= n:
            BIT [index] = max(BIT [index], value)
            index += index & (- index)
    @staticmethod
    def findLISLength(arr, n):
        GFG.coordinateCompression(arr, n)
        BIT = [0 for _ in range(n + 1)]
        for i in range(0, n + 1):
            BIT [i] = 0
        for i in range(0, n):
            GFG.update(BIT, arr [i], n)
        ans = GFG.query(BIT, n, n)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [6, 5, 1, 3, 2, 4, 8, 7]
        n = len(arr)
        ans = GFG.findLISLength(arr, n)
        print(ans)
