class GFG:
    MAX = 1000001
    primeUpto = [0 for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        isPrime = [0 for _ in range(GFG.MAX)]
        i = 0
        while i < GFG.MAX:
            isPrime [i] = 1
            i += 1
        isPrime [0] = isPrime [1] = 0
        i = 2
        while i * i < GFG.MAX:
            if isPrime [i] == 1:
                j = i * 2
                while j < GFG.MAX:
                    isPrime [j] = 0
                    j += i
            i += 1
        i = 1
        while i < GFG.MAX:
            GFG.primeUpto [i] = GFG.primeUpto [i - 1]
            if isPrime [i] == 1:
                GFG.primeUpto [i] += 1
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countOfNumbers(N, K):
        GFG.SieveOfEratosthenes()
        low = 1
        high = N
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            if mid - GFG.primeUpto [mid] >= K:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        ans = N - ans + 1 if ans != 0 else 0
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 10
        K = 3
        print(GFG.countOfNumbers(N, K))
