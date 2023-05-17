class GFG:
    @staticmethod
    def centered_cube(n):
        return (2 * n + 1) * (n * n + n + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(str(n) + "th Centered" + " cube number: ", end = '')
        print(GFG.centered_cube(n))
        n = 10
        print(str(n) + "th Centered" + " cube number: ", end = '')
        print(GFG.centered_cube(n))
