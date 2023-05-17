import math

class Solution:
    @staticmethod
    def isExists(a, n):
        freq = {}
        sum = 0
        for i in range(0, n):
            freq[a [i]] = 0 if freq[a [i]] is None else freq[a [i]] + 1
            sum += a [i]
        if math.fmod(sum, 2) == 0:
            if freq[math.trunc(sum / float(2))] is not None:
                return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [5, 1, 2, 2]
        n = len(a)
        if Solution.isExists(a, n):
            print("Yes")
        else:
            print("No")
