import math

class GFG:
    memo = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(32)]
    @staticmethod
    def dp(pos, fl, pr, bin):
        if pos == len(bin):
            return 1
        if GFG.memo [pos][fl][pr] != - 1:
            return GFG.memo [pos][fl][pr]
        val = 0
        if bin[pos] == '0':
            val = val + GFG.dp(pos + 1, fl, 0, bin)
        elif bin[pos] == '1':
            val = val + GFG.dp(pos + 1, 1, 0, bin)
        if pr == 0:
            if fl == 1:
                val += GFG.dp(pos + 1, fl, 1, bin)
            elif bin[pos] == '1':
                val += GFG.dp(pos + 1, fl, 1, bin)
        return GFG.memo [pos][fl][pr] = val
    @staticmethod
    def findIntegers(num):
        bin = ""
        while num > 0:
            if math.fmod(num, 2) == 1:
                bin += "1"
            else:
                bin += "0"
            num = math.trunc(num / float(2))
        bin = GFG.reverse(bin)
        for i in range(0, 32):
            for j in range(0, 2):
                for l in range(0, 2):
                    GFG.memo [i][j][l] = - 1
        return GFG.dp(0, 0, 0, bin)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def reverse(input):
        a = input.toCharArray()
        l = 0
        r = len(a) - 1
        l = 0
        while l < r:
            temp = a [l]
            a [l] = a [r]
            a [r] = temp
            l += 1
            r -= 1
        return str(a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 12
        print(GFG.findIntegers(N))
