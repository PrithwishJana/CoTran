import math

class GFG:
    @staticmethod
    def decToBinary(n):
        binaryNum = [0 for _ in range(32)]
        i = 0
        while n > 0:
            binaryNum [i] = math.fmod(n, 2)
            n = math.trunc(n / float(2))
            i += 1
        binary = ""
        for j in range(i - 1, -1, -1):
            binary += str(binaryNum [j])
        return binary
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countFreq(pat, txt):
        M = len(pat)
        N = len(txt)
        res = 0
        i = 0
        while i <= N - M:
            j = 0
            for j in range(0, M):
                if txt[i + j] != pat[j]:
                    break
            if j == M:
                res += 1
                j = 0
            i += 1
        return res
    @staticmethod
    def findOccurrence(arr, n, pattern):
        for i in range(0, n):
            binary = GFG.decToBinary(arr [i])
            print(GFG.countFreq(pattern, binary) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 106, 7, 8]
        pattern = "10"
        n = len(arr)
        GFG.findOccurrence(arr, n, pattern)
