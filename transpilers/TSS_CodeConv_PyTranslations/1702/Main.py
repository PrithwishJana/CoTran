class solution:
    @staticmethod
    def countPairs(arr, n):
        count = 0
        i = 0
        while i < n - 1:
            for j in range(i + 1, n):
                if arr [i] * arr [j] > arr [i] + arr [j]:
                    count += 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 0, 3, 1, 2]
        n = len(arr)
        print(solution.countPairs(arr, n))
