class GFG:
    @staticmethod
    def findOptimalSolution(a, N):
        Arrays.sort(a)
        points = 0
        for i in range(0, N):
            points += a [i] * i
        return points
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 4, 2, 3, 9]
        N = len(a)
        print(GFG.findOptimalSolution(a, N))
