class GFG:
    MAX = 256
    @staticmethod
    def lastNonRepeating(str, n):
        freq = [0 for _ in range(GFG.MAX)]
        for i in range(0, n):
            freq [str[i]] += 1
        for i in range(n - 1, -1, -1):
            ch = str[i]
            if freq [ch] == 1:
                return ("" + ch)
        return "-1"
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "GeeksForGeeks"
        n = len(str)
        print(GFG.lastNonRepeating(str, n))
