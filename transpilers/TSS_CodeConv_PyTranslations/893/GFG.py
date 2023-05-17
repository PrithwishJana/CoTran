class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumber(N, S):
        countElements = 0
        currSum = 0
        while currSum <= S:
            currSum += N
            N -= 1
            countElements += 1
        return countElements
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 0
        S = 0
        N = 5
        S = 11
        count = GFG.countNumber(N, S)
        print(count)
