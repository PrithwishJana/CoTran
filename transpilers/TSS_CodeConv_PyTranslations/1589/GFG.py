class GFG:
    @staticmethod
    def maxSubseq(vec, n):
        suffix = 0
        for i in range(n - 1, -1, -1):
            if vec [i] == 1:
                suffix += 1
                vec [i] = suffix
        res = 0
        zero = 0
        for i in range(0, n):
            if vec [i] == 0:
                zero += 1
            if vec [i] > 0:
                res = max(res, zero + vec [i])
        return max(res, zero)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = [0, 1, 0, 0, 1, 0]
        n = len(input)
        print(GFG.maxSubseq(input, n))
