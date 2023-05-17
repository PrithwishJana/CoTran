class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countCubes(a, b):
        cnt = 0
        for i in range(a, b + 1):
            j = 1
            while j * j * j <= i:
                if j * j * j == i:
                    cnt += 1
                j += 1
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 7
        b = 30
        print("Count of Cubes is " + str(GFG.countCubes(a, b)), end = '')
