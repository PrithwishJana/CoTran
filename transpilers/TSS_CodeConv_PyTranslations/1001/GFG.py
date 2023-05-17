import math

class GFG:
    MAX = 25
    @staticmethod
    def getMinSum(arr, n):
        bits_count = [0 for _ in range(GFG.MAX)]
        max_bit = 0
        sum = 0
        ans = 0
        for d in range(0, n):
            e = arr [d]
            f = 0
            while e > 0:
                rem = math.fmod(e, 2)
                e = math.trunc(e / float(2))
                if rem == 1:
                    bits_count [f] += rem
                f += 1
            max_bit = max(max_bit, f)
        for d in range(0, max_bit):
            temp = int(2) ** d
            if bits_count [d] > math.trunc(n / float(2)):
                ans = ans + temp
        for d in range(0, n):
            arr [d] = arr [d] ^ ans
            sum = sum + arr [d]
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 5, 7, 11, 15]
        n = len(arr)
        print(GFG.getMinSum(arr, n))
