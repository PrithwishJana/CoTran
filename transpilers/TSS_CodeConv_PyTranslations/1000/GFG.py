class GFG:
    MAX = 100005
    isPrime = [False for _ in range(MAX)]
    @staticmethod
    def sieveOfEratostheneses():
        GFG.isPrime [1] = True
        i = 2
        while i * i < GFG.MAX:
            if not GFG.isPrime [i]:
                j = 2 * i
                while j < GFG.MAX:
                    GFG.isPrime [j] = True
                    j += i
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findPrime(n):
        num = n + 1
        while num > 0:
            if not GFG.isPrime [num]:
                return num
            num = num + 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minNumber(arr, n):
        GFG.sieveOfEratostheneses()
        sum = 0
        for i in range(0, n):
            sum += arr [i]
        if not GFG.isPrime [sum]:
            return 0
        num = GFG.findPrime(sum)
        return num - sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 6, 8, 12]
        n = len(arr)
        print(GFG.minNumber(arr, n))
