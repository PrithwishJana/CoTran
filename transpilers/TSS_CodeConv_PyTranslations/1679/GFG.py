import math

class GFG:
    MAX = 32
    pow2 = [0 for _ in range(MAX)]
    visited = [False for _ in range(MAX)]
    ans = list  ()
    @staticmethod
    def power_2():
        ans = 1
        i = 0
        while i < GFG.MAX:
            GFG.pow2 [i] = ans
            ans *= 2
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(x):
        setBits = 0
        while x != 0:
            x = x & (x - 1)
            setBits += 1
        return setBits
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def add(num):
        point = 0
        value = 0
        i = 0
        while i < GFG.MAX:
            if GFG.visited [i]:
                i += 1
                continue
            else:
                if math.fmod(num, 2) == 1:
                    value += (1 << i)
                num = math.trunc(num / float(2))
            i += 1
        GFG.ans.append(value)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(n, k):
        GFG.ans.append(k)
        countk = GFG.countSetBits(k)
        if GFG.pow2 [countk] < n:
            print(- 1, end = '')
            return
        count = 0
        i = 0
        while i < GFG.pow2 [countk] - 1:
            GFG.add(i)
            count += 1
            if count == n:
                break
            i += 1
        for i in range(0, n):
            print(str(GFG.ans[i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        k = 5
        GFG.power_2()
        GFG.solve(n, k)
