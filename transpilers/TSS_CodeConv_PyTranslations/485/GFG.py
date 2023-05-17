class GFG:
    @staticmethod
    def sumOfSubstrings(num):
        n = len(num)
        sumofdigit = [0 for _ in range(n)]
        sumofdigit [0] = num[0] - '0'
        res = sumofdigit [0]
        for i in range(1, n):
            numi = num[i] - '0'
            sumofdigit [i] = (i + 1) * numi + 10 * sumofdigit [i - 1]
            res += sumofdigit [i]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = "1234"
        print(GFG.sumOfSubstrings(num))
