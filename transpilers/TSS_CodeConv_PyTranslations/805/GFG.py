class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxFreq(s, a, b):
        fre = [0 for _ in range(10)]
        n = len(s)
        if a > b:
            temp = a
            a = b
            b = temp
        for i in range(0, n):
            fre [s[i] - '0'] += 1
        if fre [a] == 0 and fre [b] == 0:
            return - 1
        elif fre [a] >= fre [b]:
            return a
        else:
            return b
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 4
        b = 7
        s = "47744"
        print(GFG.maxFreq(s, a, b), end = '')
