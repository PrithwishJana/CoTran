class GFG:
    @staticmethod
    def compute_lps(s):
        n = len(s)
        lps = [0 for _ in range(n)]
        len = 0
        lps [0] = 0
        i = 1
        while i < n:
            if s[i] == s[len]:
                len += 1
                lps [i] = len
                i += 1
            else:
                if len != 0:
                    len = lps [len - 1]
                else:
                    lps [i] = 0
                    i += 1
        return lps
    @staticmethod
    def Longestsubstring(s):
        lps = GFG.compute_lps(s)
        n = len(s)
        if lps [n - 1] == 0:
            print(- 1)
            return
        i = 0
        while i < n - 1:
            if lps [i] == lps [n - 1]:
                print(s[0:lps [i]])
                return
            i += 1
        if lps [lps [n - 1] - 1] == 0:
            print(- 1)
        else:
            print(s[0:lps [lps [n - 1] - 1]])
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "fixprefixsuffix"
        GFG.Longestsubstring(s)
