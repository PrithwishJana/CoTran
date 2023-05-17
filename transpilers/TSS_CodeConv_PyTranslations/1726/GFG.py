class GFG:
    LIMIT = 10000000
    position = [0 for _ in range(LIMIT + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        GFG.position [0] = - 1
        GFG.position [1] = - 1
        pos = 0
        for i in range(2, GFG.LIMIT + 1):
            if GFG.position [i] == 0:
                pos += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: position [i] = ++ pos;
                GFG.position [i] =  pos
                for j in range(i * 2, GFG.LIMIT + 1, i):
                    GFG.position [j] = - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.sieve()
        n = 11
        print(GFG.position [n], end = '')
