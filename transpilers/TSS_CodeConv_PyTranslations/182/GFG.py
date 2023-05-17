import math

class GFG:
    MAX = 26
    @staticmethod
    def updateFreq(str, freq):
        len = len(str)
        for i in range(0, len):
            freq [str[i] - 'a'] += 1
    @staticmethod
    def maxCount(str, patt):
        strFreq = [0 for _ in range(GFG.MAX)]
        GFG.updateFreq(str, strFreq)
        pattFreq = [0 for _ in range(GFG.MAX)]
        GFG.updateFreq(patt, pattFreq)
        ans = Integer.MAX_VALUE
        i = 0
        while i < GFG.MAX:
            if pattFreq [i] == 0:
                i += 1
                continue
            ans = min(ans, math.trunc(strFreq [i] / float(pattFreq [i])))
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        patt = "geeks"
        print(GFG.maxCount(str, patt))
