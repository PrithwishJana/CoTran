import math

class TheBestGift:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        str = br.readLine().split(" ")
        n = int(str [0])
        m = int(str [1])
        arr = [0 for _ in range(m)]
        str = br.readLine().split(" ")
        for i in range(0, n):
            arr [int(str [i]) - 1] += 1
        print(TheBestGift._getNumberOfWays2(arr, n))
    @staticmethod
    def _getNumberOfWays1(arr, n):
        count = 0
        i = 0
        while i < len(arr):
            count = count + (arr [i] * (n - arr [i]))
            i += 1
        return math.trunc(count / float(2))
    @staticmethod
    def sumNatual(n):
        return math.trunc((int(n) * (n + 1)) / float(2))
    @staticmethod
    def _getNumberOfWays2(arr, n):
        t = TheBestGift.sumNatual(n)
        for x in arr:
            t -= TheBestGift.sumNatual(x)
        return t
