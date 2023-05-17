class Test:
    arr = [1, 2, 3, 4]
    @staticmethod
    def subArray(n):
        for i in range(0, n):
            for j in range(i, n):
                for k in range(i, j + 1):
                    print(str(Test.arr [k]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("All Non-empty Subarrays")
        Test.subArray(len(Test.arr))
