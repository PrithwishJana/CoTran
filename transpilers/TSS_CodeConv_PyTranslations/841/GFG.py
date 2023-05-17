import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(a, n):
        P = [0 for _ in range(n)]
        P [0] = a [0]
        for i in range(1, n):
            P [i] = a [i] + P [i - 1]
        S = P [n - 1]
        hash = {}
        for i in range(0, n):
            hash[P [i]] = 1
        res = java.util.HashSet()
        i = 1
        while i * i <= S:
            if math.fmod(S, i) == 0:
                pres = True
                div1 = i
                div2 = math.trunc(S / float(i))
                for j in range(div1, S + 1, div1):
                    if hash[j] is None or hash[j] != 1:
                        pres = False
                        break
                if pres and div1 != S:
                    res.add(div1)
                pres = True
                for j in range(math.trunc(S / float(i)), S + 1, math.trunc(S / float(i))):
                    if hash[j] is None or hash[j] != 1:
                        pres = False
                        break
                if pres and div2 != S:
                    res.add(div2)
            i += 1
        if res.size() == 0:
            print("-1")
            return
        for i in res:
            print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 2, 1, 1, 1, 2, 1, 3]
        n = len(a)
        GFG.getSum(a, n)
