class solution:
    @staticmethod
    def sameOccurrence(arr, n, x, y):
        result = 0
        i = 0
        while i <= n - 1:
            ctX = 0
            ctY = 0
            j = i
            while j <= n - 1:
                if arr [j] == x:
                    ctX += 1
                elif arr [j] == y:
                    ctY += 1
                if ctX == ctY:
                    result += 1
                j += 1
            i += 1
        return (result)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 2, 3, 4, 1]
        n = len(arr)
        x = 2
        y = 3
        print(solution.sameOccurrence(arr, n, x, y))
