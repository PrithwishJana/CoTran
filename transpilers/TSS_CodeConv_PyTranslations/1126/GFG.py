class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxZeros(N):
        maxm = - 1
        cnt = 0
        while N != 0:
            if (N & 1) == 0:
                cnt += 1
                N >>= 1
                maxm = max(maxm, cnt)
            else:
                maxm = max(maxm, cnt)
                cnt = 0
                N >>= 1
        return maxm
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 14
        print(GFG.maxZeros(N))
