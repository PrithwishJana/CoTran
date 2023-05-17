import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSubsequence(arr, n, k):
        M = {}
        for i in range(0, n):
            if arr [i] in M.keys():
                M[arr [i]] = M[arr [i]] + 1
            else:
                M[arr [i]] = 1
        numCount = [0 for _ in range(k + 1)]
        for i in range(0, k + 1):
            numCount [i] = 0
        itr = M.entrySet().iterator()
        while itr.hasNext():
            entry = itr.next()
            if entry.getKey() <= k:
                i = 1
                while True:
                    if entry.getKey() * i > k:
                        break
                    numCount [entry.getKey() * i] += entry.getValue()
                    i += 1
            else:
                break
        lcm = 0
        length = 0
        for i in range(1, k + 1):
            if numCount [i] > length:
                length = numCount [i]
                lcm = i
        if lcm == 0:
            print(- 1)
        else:
            print("LCM = " + str(lcm) + ", Length = " + str(length))
            print("Indexes = ", end = '')
            for i in range(0, n):
                if math.fmod(lcm, arr [i]) == 0:
                    print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 14
        arr = [2, 3, 4, 5]
        n = len(arr)
        GFG.findSubsequence(arr, n, k)
