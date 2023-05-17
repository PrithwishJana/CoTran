class GFG:
    @staticmethod
    def y(x):
        return (1 / (1 + x))
    @staticmethod
    def BooleRule(a, b):
        n = 4
        h = 0
        h = int(((b - a) / n))
        sum = 0
        bl = (7 * GFG.y(a) + 32 * GFG.y(a + h) + 12 * GFG.y(a + 2 * h) + 32 * GFG.y(a + 3 * h) + 7 * GFG.y(a + 4 * h)) * 2 * h / 45
        sum = sum + bl
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        System.out.printf(("f(x) = %.4f"), GFG.BooleRule(0, 4))
