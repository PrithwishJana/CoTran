class GFG:
    @staticmethod
    def maxAlternateSum(arr, n):
        if n == 1:
            return arr [0]
        dec = [0 for _ in range(n)]
        inc = [0 for _ in range(n)]
        dec [0] = inc [0] = arr [0]
        flag = 0
        for i in range(1, n):
            for j in range(0, i):
                if arr [j] > arr [i]:
                    dec [i] = max(dec [i], inc [j] + arr [i])
                    flag = 1
                elif arr [j] < arr [i] and flag == 1:
                    inc [i] = max(inc [i], dec [j] + arr [i])
        result = Integer.MIN_VALUE
        for i in range(0, n):
            if result < inc [i]:
                result = inc [i]
            if result < dec [i]:
                result = dec [i]
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [8, 2, 3, 5, 7, 9, 10]
        print("Maximum sum = " + str(GFG.maxAlternateSum(arr, len(arr))))
