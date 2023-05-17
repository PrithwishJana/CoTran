class Test:
    PI = Math.PI
    @staticmethod
    def findArea(r):
        return Test.PI * r ** 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("Area is " + str(Test.findArea(5)))
