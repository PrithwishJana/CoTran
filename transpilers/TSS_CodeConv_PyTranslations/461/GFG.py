class GFG:
    @staticmethod
    def findNum(div, rem, N):
        num = rem [N - 1]
        for i in range(N - 2, -1, -1):
            num = num * div [i] + rem [i]
        return num
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        div = [8, 3]
        rem = [2, 2]
        N = len(div)
        print(GFG.findNum(div, rem, N))
