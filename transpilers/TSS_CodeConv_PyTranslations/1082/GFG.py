#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.sin
class GFG:
    @staticmethod
    def cal_sin(n):
        accuracy = float(0.0001)
        denominator = 0
        sinx = 0
        sinval = 0
        n = n * float((3.142 / 180.0))
        x1 = n
        sinx = n
        sinval = float(sin(n))
        i = 1
        loop_condition = True
        while loop_condition:
            denominator = 2 * i * (2 * i + 1)
            x1 = - x1 * n * n / denominator
            sinx = sinx + x1
            i = i + 1
            loop_condition = accuracy <= sinval - sinx
        print(sinx)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 90
        GFG.cal_sin(n)
