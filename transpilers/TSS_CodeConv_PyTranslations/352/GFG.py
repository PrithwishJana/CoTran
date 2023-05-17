class GFG:
    MAX = 1000000
    prime = [False for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        Arrays.fill(GFG.prime, True)
        p = 2
        while p * p < GFG.MAX:
            if GFG.prime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    GFG.prime [i] = False
                    i += p
            p += 1
    @staticmethod
    def printPrimeQuad(n):
        i = 0
        while i < n - 7:
            if GFG.prime [i] and GFG.prime [i + 2] and GFG.prime [i + 6] and GFG.prime [i + 8]:
                print(str(i) + " " + str(i + 2) + " " + str(i + 6) + " " + str(i + 8))
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 20
        GFG.sieve()
        GFG.printPrimeQuad(n)
