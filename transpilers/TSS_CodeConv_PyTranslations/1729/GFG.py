class GFG:
    @staticmethod
    def maxCost(a, n, l, r):
        mx = 0
        k = 0
        for i in range(0, n):
            mx = max(mx, a [i])
        count = [0 for _ in range(mx + 1)]
        i = 0
        while i < len(count):
            count [i] = 0
            i += 1
        for i in range(0, n):
            count [a [i]] += 1
        res = [0 for _ in range(mx + 1)]
        res [0] = 0
        l = min(l, r)
        for num in range(1, mx + 1):
            k = max(num - l - 1, 0)
            res [num] = max(res [num - 1], num * count [num] + res [k])
        return res [mx]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 1, 2, 3, 2, 2, 1]
        l = 1
        r = 1
        n = len(a)
        print(GFG.maxCost(a, n, l, r))
