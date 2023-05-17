class GFG:
    MAX = 100001
    perfectDiv = [0 for _ in range(MAX)]
    @staticmethod
    def precomputeCounts():
        i = 1
        while i * i < GFG.MAX:
            j = i * i
            while j < GFG.MAX:
                GFG.perfectDiv [j] += 1
                j += i * i
            i += 1
    @staticmethod
    def countPerfectDivisors(n):
        return GFG.perfectDiv [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.precomputeCounts()
        n = 16
        print("Total perfect divisors of " + str(n) + " = " + str(GFG.countPerfectDivisors(n)))
        n = 12
        print("Total perfect divisors of " + str(n) + " = " + str(GFG.countPerfectDivisors(n)))
