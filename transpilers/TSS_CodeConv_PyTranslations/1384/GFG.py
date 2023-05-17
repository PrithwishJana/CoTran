class GFG:
    @staticmethod
    def countSubSeq(i, sum, cnt, a, n):
        if i == n:
            if sum == 0 and cnt > 0:
                return 1
            else:
                return 0
        ans = 0
        ans += GFG.countSubSeq(i + 1, sum, cnt, a, n)
        ans += GFG.countSubSeq(i + 1, sum + a [i], cnt + 1, a, n)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [- 1, 2, - 2, 1]
        n = len(a)
        print(GFG.countSubSeq(0, 0, 0, a, n))
