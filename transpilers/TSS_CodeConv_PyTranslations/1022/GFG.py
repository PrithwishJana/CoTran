class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSteps(n):
        steps = 0
        while n > 0:
            largest = int(Math.cbrt(n))
            n -= (largest * largest * largest)
            steps += 1
        return steps
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 150
        print(GFG.countSteps(n), end = '')
