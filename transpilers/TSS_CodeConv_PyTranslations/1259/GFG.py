class GFG:
    MAX_CHAR = chr(26)
    @staticmethod
    def distributingBalls(k, n, str):
        a = [0 for _ in range(GFG.MAX_CHAR)]
        for i in range(0, n):
            a [str[i] - 'a'] += 1
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            if a [i] > k:
                return False
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        k = 3
        str = "aacaab"
        if GFG.distributingBalls(k, n, str):
            print("YES")
        else:
            print("NO")
