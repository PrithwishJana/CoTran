class GFG:
    @staticmethod
    def maxOperations(str):
        i = 0
        g = 0
        gk = 0
        gks = 0
        i = g = gk = gks = 0
        i = 0
        while i < len(str):
            if str[i] == 'g':
                g += 1
            elif str[i] == 'k':
                if g > 0:
                    g -= 1
                    gk += 1
            elif str[i] == 's':
                if gk > 0:
                    gk -= 1
                    gks += 1
            i += 1
        return gks
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = "ggkssk"
        print(GFG.maxOperations(a), end = '')
