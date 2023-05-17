class GFG:
    @staticmethod
    def minOperations(arr, n):
        maxi = 0
        result = 0
        freq = [0 for _ in range(1000001)]
        for i in range(0, n):
            x = arr [i]
            freq [x] += 1
        maxi = java.util.Arrays.stream(arr).max().getAsInt()
        for i in range(1, maxi + 1):
            if freq [i] != 0:
                for j in range(i * 2, maxi + 1, i):
                    freq [j] = 0
                result += 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 2, 4, 4, 4]
        n = len(arr)
        print(GFG.minOperations(arr, n))
