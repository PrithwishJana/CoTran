import math

class GFG:
    @staticmethod
    def product(x):
        prod = 1
        while x > 0:
            prod *= (math.fmod(x, 10))
            x = math.trunc(x / float(10))
        return prod
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNumber(l, r):
        b = str(r)
        ans = r
        i = 0
        while i < len(b):
            if b[i] == '0':
                i += 1
                continue
            curr = b.toCharArray()
            curr [i] = chr(((int((curr [i] - ord('0'))) - 1) + ord(('0'))))
            j = i + 1
            while j < len(curr):
                curr [j] = '9'
                j += 1
            num = 0
            j = 0
            while j < len(curr):
                num = num * 10 + (curr [j] - '0')
                j += 1
            if num >= l and GFG.product(ans) < GFG.product(num):
                ans = num
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 1
        r = 10
        print(GFG.findNumber(l, r))
        l = 51
        r = 62
        print(GFG.findNumber(l, r))
