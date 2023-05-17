class GFG:
    sz = int(1e)5
    isPrime = [False for _ in range(sz + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        Arrays.fill(GFG.isPrime, True)
        GFG.isPrime [0] = GFG.isPrime [1] = False
        i = 2
        while i * i <= GFG.sz:
            if GFG.isPrime [i]:
                j = i * i
                while j < GFG.sz:
                    GFG.isPrime [j] = False
                    j += i
            i += 1
    @staticmethod
    def minDifference(L, R):
        fst = 0
        for i in range(L, R + 1):
            if GFG.isPrime [i]:
                fst = i
                break
        snd = 0
        for i in range(fst + 1, R + 1):
            if GFG.isPrime [i]:
                snd = i
                break
        if snd == 0:
            return - 1
        diff = snd - fst
        left = snd + 1
        right = R
        for i in range(left, right + 1):
            if GFG.isPrime [i]:
                if i - snd <= diff:
                    fst = snd
                    snd = i
                    diff = snd - fst
        return diff
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.sieve()
        L = 21
        R = 50
        print(GFG.minDifference(L, R))
