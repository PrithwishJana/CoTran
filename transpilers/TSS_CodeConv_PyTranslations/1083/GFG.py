class GFG:
    arr = [1, 2, 3, 4, 5, 6]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def multiply():
        pro = 1
        i = 0
        while i < len(GFG.arr):
            pro = pro * GFG.arr [i]
            i += 1
        return pro
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.multiply())
