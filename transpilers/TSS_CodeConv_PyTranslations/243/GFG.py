class GFG:
    @staticmethod
    def smallestKFreq(a, n, k):
        m = {}
        for i in range(0, n):
            if a [i] in m.keys():
                m[a [i]] = m[a [i]] + 1
            else:
                m[a [i]] = 1
        res = Integer.MAX_VALUE
        s = m.keys()
        for temp in s:
            if m[temp] == k:
                res = min(res, temp)
        return res if (res != Integer.MAX_VALUE) else - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 2, 1, 3, 1]
        k = 2
        print(GFG.smallestKFreq(arr, len(arr), k))
