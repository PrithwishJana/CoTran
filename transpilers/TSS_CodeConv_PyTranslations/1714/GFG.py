class GFG:
    @staticmethod
    def getPerfectSquares(n):
        perfectSquares = []
        current = 1
        i = 1
        while current <= n:
            perfectSquares.append(current)
            i += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: current = (int) Math.pow(++ i, 2);
            current = int(i) ** 2
        return perfectSquares
    @staticmethod
    def maxPairSum(arr):
        n = len(arr)
        max = 0
        secondMax = 0
        if arr [0] > arr [1]:
            max = arr [0]
            secondMax = arr [1]
        else:
            max = arr [1]
            secondMax = arr [0]
        for i in range(2, n):
            if arr [i] > max:
                secondMax = max
                max = arr [i]
            elif arr [i] > secondMax:
                secondMax = arr [i]
        return (max + secondMax)
    @staticmethod
    def countPairsWith(n, perfectSquares, nums):
        count = 0
        for i, unusedItem in enumerate(perfectSquares):
            temp = perfectSquares[i] - n
            if temp > n and nums.contains(temp):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(arr):
        i = 0
        n = len(arr)
        max = GFG.maxPairSum(arr)
        perfectSquares = GFG.getPerfectSquares(max)
        nums = HashSet()
        for i in range(0, n):
            nums.add(arr [i])
        count = 0
        for i in range(0, n):
            count += GFG.countPairsWith(arr [i], perfectSquares, nums)
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 6, 9, 10, 20]
        print(GFG.countPairs(arr))
