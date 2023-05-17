class GFG:
    sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    @staticmethod
    def countSticks(str, n):
        cnt = 0
        for i in range(0, n):
            cnt += (GFG.sticks [str[i] - '0'])
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "56"
        n = len(str)
        print(GFG.countSticks(str, n))
