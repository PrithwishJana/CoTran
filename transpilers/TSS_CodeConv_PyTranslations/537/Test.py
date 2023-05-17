class Test:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(1 if Test.isPower(10, 1) else 0)
        print(1 if Test.isPower(1, 20) else 0)
        print(1 if Test.isPower(2, 128) else 0)
        print(1 if Test.isPower(2, 30) else 0)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPower(x, y):
        if x == 1:
            return (y == 1)
        pow = 1
        while pow < y:
            pow = pow * x
        return (pow == y)
