class GFG:
    @staticmethod
    def arePermutations(a, b, n, m):
        sum1 = 0
        sum2 = 0
        mul1 = 1
        mul2 = 1
        for i in range(0, n):
            sum1 += a [i]
            mul1 *= a [i]
        for i in range(0, m):
            sum2 += b [i]
            mul2 *= b [i]
        return ((sum1 == sum2) and (mul1 == mul2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 3, 2]
        b = [3, 1, 2]
        n = len(a)
        m = len(b)
        if GFG.arePermutations(a, b, n, m) == True:
            print("Yes")
        else:
            print("No")
