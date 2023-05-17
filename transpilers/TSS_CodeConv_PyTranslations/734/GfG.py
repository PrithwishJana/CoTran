class GfG:
    @staticmethod
    def minCost(n, arr, cost):
        sum = 0
        totalCost = 0
        i = 0
        while i < n - 1:
            sum += arr [i]
            i += 1
        totalCost += cost * sum
        arr [n - 1] += sum
        totalCost += (2 * cost * arr [n - 1])
        return totalCost
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 4, 5]
        n = len(arr)
        cost = 1
        print(GfG.minCost(n, arr, cost))
