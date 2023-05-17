class GFG:
    dp = [[[0 for _ in range(162)] for _ in range(2)] for _ in range(18)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(i, tight, sum_so_far, Sum, number, len):
        if i == len:
            if sum_so_far == Sum:
                return 1
            else:
                return 0
        ans = GFG.dp [i][1][sum_so_far]
        if ans != - 1:
            return ans
        ans = 0
        ntight = False
        nsum_so_far = 0
        for currdigit in range('0', '9' + 1):
            if (not tight) and currdigit > number[i]:
                break
            ntight = tight or currdigit < number[i]
            nsum_so_far = sum_so_far + (currdigit - '0')
            ans += GFG.solve(i + 1, ntight, nsum_so_far, Sum, number, len)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        count = 0
        sum = 4
        number = "100"
        for i in range(0, 18):
            for j in range(0, 2):
                for k in range(0, 162):
                    GFG.dp [i][j][k] = - 1
        print(GFG.solve(0, False, 0, sum, number, len(number)))
