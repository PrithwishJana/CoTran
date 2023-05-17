class solution:
    @staticmethod
    def countSubArrays(arr, n, K):
        count = 0
        for i in range(0, n):
            for j in range(i, n):
                bitwise_or = 0
                for k in range(i, j + 1):
                    bitwise_or = bitwise_or | arr [k]
                if bitwise_or >= K:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 4, 5]
        n = len(arr)
        k = 6
        print(solution.countSubArrays(arr, n, k))
