class GFG:
    MAX = 100001
    isPrime = [0 for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        p = 2
        while p * p < GFG.MAX:
            if GFG.isPrime [p] == 0:
                i = p * 2
                while i < GFG.MAX:
                    GFG.isPrime [i] = 1
                    i += p
            p += 1
        return - 1
    @staticmethod
    def findSubset(a, n):
        cnt1 = 0
        for i in range(0, n):
            if a [i] == 1:
                cnt1 += 1
        if cnt1 > 0:
            for i in range(0, n):
                if (a [i] != 1) and (GFG.isPrime [a [i] + 1] == 0):
                    print(cnt1 + 1)
                    for j in range(0, cnt1):
                        print(str(1) + " ", end = '')
                    print(a [i])
                    return 0
        if cnt1 >= 2:
            print(cnt1)
            for i in range(0, cnt1):
                print(str(1) + " ", end = '')
            print()
            return 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if GFG.isPrime [a [i] + a [j]] == 0:
                    print(2)
                    print(str(a [i]) + " " + str(a [j]))
                    return 0
        print(- 1)
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.sieve()
        A = [2, 1, 1]
        n = len(A)
        GFG.findSubset(A, n)
