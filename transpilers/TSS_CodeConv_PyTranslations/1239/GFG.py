import math

class GFG:
    @staticmethod
    def NthCharacter(n):
        s = ""
        c = 1
        i = 1
        while True:
            if c < 10:
                s += str(c)
            else:
                s1 = ""
                dup = c
                while dup > 0:
                    s1 += str(math.fmod(dup, 10))
                    dup = math.trunc(dup / float(10))
                temp = StringBuilder()
                temp.append(s1)
                temp = temp.reverse()
                s += temp
            c += 1
            if len(s) >= n:
                return s[n - 1]
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 11
        print(GFG.NthCharacter(n))
