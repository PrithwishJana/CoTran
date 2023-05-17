import math

class GFG:
    @staticmethod
    def findRepeatingNumber(arr, n):
        sq = int(math.sqrt(n))
        range = (math.trunc(n / float(sq))) + 1
        count = [0 for _ in range(range)]
        for i in range(0, n + 1):
            count [math.trunc((arr [i] - 1) / float(sq))] += 1
        selected_block = range - 1
        i = 0
        while i < range - 1:
            if count [i] > sq:
                selected_block = i
                break
            i += 1
        m = {}
        for i in range(0, n + 1):
            if ((selected_block * sq) < arr [i]) and (arr [i] <= ((selected_block + 1) * sq)):
                m[arr [i]] = 1
                if m[arr [i]] == 1:
                    return arr [i]
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 2, 3, 5, 4]
        n = 5
        print("One of the numbers repeated in the array is: " + str(GFG.findRepeatingNumber(arr, n)))
