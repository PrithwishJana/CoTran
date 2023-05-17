class GFG:
    @staticmethod
    def getLevenstein(input):
        revInput = StringBuilder(input)
        revInput = revInput.reverse()
        n = input.length()
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp [0][i] = i
            dp [i][0] = i
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if input.charAt(i - 1) == revInput.charAt(j - 1):
                    dp [i][j] = dp [i - 1][j - 1]
                else:
                    dp [i][j] = 1 + min(dp [i - 1][j], dp [i][j - 1])
        res = Integer.MAX_VALUE
        i = n
        j = 0
        while i >= 0:
            res = min(res, dp [i][j])
            if i < n:
                res = min(res, dp [i + 1][j])
            if i > 0:
                res = min(res, dp [i - 1][j])
            i -= 1
            j += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = StringBuilder("myfirstgeekarticle")
        print(GFG.getLevenstein(input))
