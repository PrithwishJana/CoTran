class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n):
        counter = 0
        for i in range(1, n):
            for j in range(i, n):
                for k in range(j, n):
                    for l in range(k, n):
                        if i + j + k + l == n:
                            counter += 1
        return counter
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 8
        print(GFG.countWays(n))
