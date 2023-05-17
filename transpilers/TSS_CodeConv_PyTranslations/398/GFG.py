class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countTriplets(A, B, C):
        ans = 0
        for i in range(1, A + 1):
            for j in range(1, B + 1):
                for k in range(1, C + 1):
                    if i * k > j * j:
                        ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = 3
        B = 2
        C = 2
        print(GFG.countTriplets(A, B, C))
