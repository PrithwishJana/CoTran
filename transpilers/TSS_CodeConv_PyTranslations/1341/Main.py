class Test:
    @staticmethod
    def printCubes(a, b):
        for i in range(a, b + 1):
            j = 1
            while j * j * j <= i:
                if j * j * j == i:
                    print(str(j * j * j) + "  ", end = '')
                    break
                j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 1
        b = 100
        print("Perfect cubes in given range:")
        Test.printCubes(a, b)
