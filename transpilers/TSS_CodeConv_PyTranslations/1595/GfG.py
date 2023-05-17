import math

class GfG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def print(a, n, ind):
        i = ind
        while i < n + ind:
            print(a [(math.fmod(i, n))] + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        a = ['A', 'B', 'C', 'D', 'E', 'F']
        n = 6
        GfG.print(a, n, 3)
