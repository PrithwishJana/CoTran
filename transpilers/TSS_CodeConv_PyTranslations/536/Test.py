class Test:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("True" if Test.isPower(10, 1) else "False")
        print("True" if Test.isPower(1, 20) else "False")
        print("True" if Test.isPower(2, 128) else "False")
        print("True" if Test.isPower(2, 30) else "False")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPower(x, y):
        if x == 1:
            return (y == 1)
        pow = 1
        while pow < y:
            pow = pow * x
        return (pow == y)
