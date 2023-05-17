import math

class GFG:
    @staticmethod
    def find_k(a, b):
        if math.fmod((a + b), 2) == 0:
            return (math.trunc((a + b) / float(2)))
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 16
        print(GFG.find_k(a, b))
