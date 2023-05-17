import math

class GFG:
    s = ""
    @staticmethod
    def ReverseString(s):
        arr = s.toCharArray()
        i = 0
        while i < math.trunc(len(arr) / float(2)):
            temp = arr [i]
            arr [i] = arr [len(arr) - i - 1]
            arr [len(arr) - i - 1] = temp
            i += 1
        return str(arr)
    @staticmethod
    def binary_conversion(m):
        while m != 0:
            tmp = math.fmod(m, 2)
            GFG.s += str(tmp)
            m = int((math.trunc(m / float(2))))
        GFG.s = GFG.ReverseString(GFG.s)
    @staticmethod
    def find_character(n, m, i):
        GFG.binary_conversion(m)
        s1 = ""
        for x in range(0, n):
            y = 0
            while y < len(GFG.s):
                if GFG.s[y] == '1':
                    s1 += "10"
                else:
                    s1 += "01"
                y += 1
            GFG.s = s1
            s1 = ""
        return GFG.s[i] - '0'
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = 5
        n = 2
        i = 8
        print(GFG.find_character(n, m, i), end = '')
