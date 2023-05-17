import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(n):
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def totalPairs(arr, n):
        m = {}
        for i in range(0, n):
            count = GFG.countSetBits(arr [i])
            if count in m.keys():
                m[count] = m[count] + 1
            else:
                m[count] = 1
        result = 0
        for entry in m.entrySet():
            value = entry.getValue()
            result += (math.trunc((value * (value - 1)) / float(2)))
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [7, 5, 3, 9, 1, 2]
        n = len(arr)
        print(GFG.totalPairs(arr, n))
