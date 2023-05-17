class GFG:
    @staticmethod
    def sqroot(s):
        pSq = 0
        N = 0
        for i in range(int((s)), 0, -1):
            for j in range(1, i):
                if j * j == i:
                    pSq = i
                    N = j
                    break
            if pSq > 0:
                break
        d = s - pSq
        P = d / (2.0f * N)
        A = N + P
        sqrt_of_s = A - ((P * P) / (2.0f * A))
        return sqrt_of_s
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 9.2345f
        sqroot_of_num = GFG.sqroot(num)
        print("Square root of " + str(num) + " = " + round(sqroot_of_num * 100000.0) / 100000.0)
