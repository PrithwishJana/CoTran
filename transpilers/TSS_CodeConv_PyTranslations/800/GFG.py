import math

class GFG:
    @staticmethod
    def K_String(s, k):
        n = len(s)
        fre = [0 for _ in range(26)]
        for i in range(0, n):
            fre [s[i] - 'a'] += 1
        str = ""
        for i in range(0, 26):
            if math.fmod(fre [i], k) == 0:
                x = math.trunc(fre [i] / float(k))
                while x != 0:
                    str += chr((i + 'a'))
                    x -= 1
            else:
                return "-1"
        return str
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "aabb"
        k = 2
        print(GFG.K_String(s, k))
