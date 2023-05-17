class solution:
    def compare(self, a, b):
        return a > b
    @staticmethod
    def findMaxOR(arr, n):
        temp = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if arr [i] < arr [j]:
                    temp = arr [i]
                    arr [i] = arr [j]
                    arr [j] = temp
        maxOR = arr [0]
        count = 1
        for i in range(1, n):
            if (maxOR | arr [i]) > maxOR:
                maxOR = maxOR | arr [i]
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arrgs):
        arr = [5, 1, 3, 4, 2]
        n = len(arr)
        print(solution.findMaxOR(arr, n))
