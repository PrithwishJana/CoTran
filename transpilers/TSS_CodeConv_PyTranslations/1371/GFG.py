class GFG:
    @staticmethod
    def countOcc(s):
        cnt = 0
        i = 0
        while i < len(s) - 3:
            c = 0
            l = 0
            a = 0
            p = 0
            j = i
            while j < i + 4:
                if s[j] == 'c':
                    c += 1
                elif s[j] == 'l':
                    l += 1
                elif s[j] == 'a':
                    a += 1
                elif s[j] == 'p':
                    p += 1
                j += 1
            if c == 1 and l == 1 and a == 1 and p == 1:
                cnt += 1
            i += 1
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "clapc"
        print(GFG.countOcc(s.casefold()), end = '')
