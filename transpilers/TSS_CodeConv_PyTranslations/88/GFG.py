class GFG:
    @staticmethod
    def centered_square_num(n):
        return n * n + ((n - 1) * (n - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        print(str(n) + "th Centered" + " square number: " + str(GFG.centered_square_num(n)))
