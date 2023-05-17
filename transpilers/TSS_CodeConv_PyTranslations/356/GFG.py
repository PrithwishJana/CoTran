class GFG:
    MAX = 1000
    sequence = [0 for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def vanEckSequence():
        i = 0
        while i < GFG.MAX - 1:
            GFG.sequence [i] = 0
            i += 1
        i = 0
        while i < GFG.MAX - 1:
            for j in range(i - 1, -1, -1):
                if GFG.sequence [j] == GFG.sequence [i]:
                    GFG.sequence [i + 1] = i - j
                    break
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getNthTerm(n):
        return GFG.sequence [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.vanEckSequence()
        n = 6
        print(GFG.getNthTerm(n))
        n = 100
        print(GFG.getNthTerm(n))
