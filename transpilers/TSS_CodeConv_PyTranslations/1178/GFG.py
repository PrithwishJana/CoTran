class GFG:
    @staticmethod
    def countSolutions(a):
        count = 0
        for i in range(0, a + 1):
            if a == (i + (a ^ i)):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 3
        print(GFG.countSolutions(a))
