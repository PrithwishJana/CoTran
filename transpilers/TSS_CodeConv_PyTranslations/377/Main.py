class Test:
    @staticmethod
    def countWindowDistinct(win, k):
        dist_count = 0
        for i in range(0, k):
            j = 0
            for j in range(0, i):
                if win [i] == win [j]:
                    break
            if j == i:
                dist_count += 1
        return dist_count
    @staticmethod
    def countDistinct(arr, n, k):
        i = 0
        while i <= n - k:
            print(Test.countWindowDistinct(arr[i:len(arr)], k))
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 1, 3, 4, 2, 3]
        k = 4
        Test.countDistinct(arr, len(arr), k)
