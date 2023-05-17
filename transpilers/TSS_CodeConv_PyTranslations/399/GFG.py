class GFG:
    MAX = 100000
    prime = [False for _ in range(MAX + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        i = 0
        while i < GFG.MAX + 1:
            GFG.prime [i] = True
            i += 1
        p = 2
        while p * p <= GFG.MAX:
            if GFG.prime [p] == True:
                i = p * p
                while i <= GFG.MAX:
                    GFG.prime [i] = False
                    i += p
            p += 1
    @staticmethod
    def smallestPrime(d):
        l = int(10) ** (d - 1)
        r = int(10) ** d - 1
        for i in range(l, r + 1):
            if GFG.prime [i]:
                return i
        return - 1
    @staticmethod
    def largestPrime(d):
        l = int(10) ** (d - 1)
        r = int(10) ** d - 1
        for i in range(r, l - 1, -1):
            if GFG.prime [i]:
                return i
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        queries = [2, 5]
        q = len(queries)
        for i in range(0, q):
            print(str(GFG.smallestPrime(queries [i])) + " " + str(GFG.largestPrime(queries [i])))
