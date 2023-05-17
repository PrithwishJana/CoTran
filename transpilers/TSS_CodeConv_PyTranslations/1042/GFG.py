import math

class GFG:
    @staticmethod
    def minimalSteps(s, n):
        dp = [0 for _ in range(n)]
        for i in range(0, n):
            dp [i] = Integer.MAX_VALUE
        s1 = ""
        s2 = ""
        dp [0] = 1
        s1 += s[0]
        for i in range(1, n):
            s1 += s[i]
            s2 = s[i + 1:i + 1]
            dp [i] = min(dp [i], dp [i - 1] + 1)
            if s1 is s2:
                dp [i * 2 + 1] = min(dp [i] + 1, dp [i * 2 + 1])
        return dp [n - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aaaaaaaa"
        n = len(s)
        print(math.trunc(GFG.minimalSteps(s, n) / float(2)))
