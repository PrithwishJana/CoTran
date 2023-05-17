class GFG:
    MAX = 100
    @staticmethod
    def countSubsequence(s, n):
        cntG = 0
        cntF = 0
        result = 0
        C = 0
        for i in range(0, n):
            if s[i] == 'G':
                cntG += 1
                result += C
            elif s[i] == 'F':
                cntF += 1
                C += cntG
            else:
                continue
        print(result)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "GFGFG"
        n = len(s)
        GFG.countSubsequence(s, n)
