class Test:
    arr1 = [1, 5, 9, 10, 15, 20]
    arr2 = [2, 3, 8, 13]
    @staticmethod
    def merge(m, n):
        for i in range(n - 1, -1, -1):
            j = 0
            last = Test.arr1 [m - 1]
            j = m - 2
            while j >= 0 and Test.arr1 [j] > Test.arr2 [i]:
                Test.arr1 [j + 1] = Test.arr1 [j]
                j -= 1
            if j != m - 2 or last > Test.arr2 [i]:
                Test.arr1 [j + 1] = Test.arr2 [i]
                Test.arr2 [i] = last
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        Test.merge(len(Test.arr1), len(Test.arr2))
        print("After Merging \nFirst Array: ", end = '')
        print(java.util.Arrays.toString(Test.arr1))
        print("Second Array: ", end = '')
        print(java.util.Arrays.toString(Test.arr2))
