class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def distinctSubString(P, Q, K, N):
        S = HashSet()
        for i in range(0, N):
            sum = 0
            s = ""
            for j in range(i, N):
                pos = P[j] - 'a'
                sum += Q[pos] - '0'
                s += P[j]
                if sum <= K:
                    S.add(s)
                else:
                    break
        return S.size()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        P = "abcde"
        Q = "12345678912345678912345678"
        K = 5
        N = len(P)
        print(GFG.distinctSubString(P, Q, K, N), end = '')
