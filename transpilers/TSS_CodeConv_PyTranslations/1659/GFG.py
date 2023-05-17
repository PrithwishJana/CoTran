class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def distinctSubString(P, N):
        S = HashSet()
        for i in range(0, N):
            freq = [False for _ in range(26)]
            s = ""
            for j in range(i, N):
                pos = P[j] - 'a'
                if freq [pos] == True:
                    break
                freq [pos] = True
                s += P[j]
                S.add(s)
        return S.size()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        S = "abba"
        N = len(S)
        print(GFG.distinctSubString(S, N), end = '')
