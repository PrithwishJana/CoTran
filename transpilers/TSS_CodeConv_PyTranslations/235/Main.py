import math

class RepeatElement:
    def printRepeating(self, arr, size):
        S = 0
        P = 1
        x = 0
        y = 0
        D = 0
        n = size - 2
        i = 0
        for i in range(0, size):
            S = S + arr [i]
            P = P * arr [i]
        S = S - math.trunc(n * (n + 1) / float(2))
        P = math.trunc(P / float(self.fact(n)))
        D = int(math.sqrt(S * S - 4 * P))
        x = math.trunc((D + S) / float(2))
        y = math.trunc((S - D) / float(2))
        print("The two repeating elements are : ", end = '')
        print(str(x) + " & " + str(y), end = '')
        print()
    def fact(self, n):
        return 1 if (n == 0) else n * self.fact(n - 1)
    @staticmethod
    def main(args):
        repeat = RepeatElement()
        arr = [4, 2, 4, 5, 2, 3, 1]
        arr_size = len(arr)
        repeat.printRepeating(arr, arr_size)
