import math

class GFG:
    @staticmethod
    def minSwaps(s1, s2):
        c0 = 0
        c1 = 0
        i = 0
        while i < len(s1):
            if s1[i] == '0' and s2[i] == '1':
                c0 += 1
            elif s1[i] == '1' and s2[i] == '0':
                c1 += 1
            i += 1
        ans = math.trunc(c0 / float(2)) + math.trunc(c1 / float(2))
        if math.fmod(c0, 2) == 0 and math.fmod(c1, 2) == 0:
            return ans
        elif math.fmod((c0 + c1), 2) == 0:
            return ans + 2
        else:
            return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s1 = "0011"
        s2 = "1111"
        ans = GFG.minSwaps(s1, s2)
        print(ans)
