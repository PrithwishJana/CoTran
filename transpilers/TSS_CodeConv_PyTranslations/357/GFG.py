﻿class GFG:
    MAX = 100000
    sequence = [0 for _ in range(MAX + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def vanEckSequence():
        i = 0
        while i < GFG.MAX:
            GFG.sequence [i] = 0
            i += 1
        i = 0
        while i < GFG.MAX:
            for j in range(i - 1, -1, -1):
                if GFG.sequence [j] == GFG.sequence [i]:
                    GFG.sequence [i + 1] = i - j
                    break
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getCount(n):
        count = 1
        i = n - 1
        while GFG.sequence [i + 1] != 0:
            count += 1
            i = i - GFG.sequence [i + 1]
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.vanEckSequence()
        n = 5
        print(GFG.getCount(n))
        n = 11
        print(GFG.getCount(n))
