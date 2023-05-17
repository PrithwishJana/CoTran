import math

class Solution:
    MAX = 10000
    hashTable = [0 for _ in range(MAX)]
    @staticmethod
    def minOperations(arr, n):
        Arrays.sort(arr)
        for i in range(0, n):
            Solution.hashTable [arr [i]] += 1
        res = 0
        for i in range(0, n):
            if Solution.hashTable [arr [i]] != 0:
                for j in range(i, n):
                    if math.fmod(arr [j], arr [i]) == 0:
                        Solution.hashTable [arr [j]] = 0
                res += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 6, 2, 8, 7, 21, 24, 49, 44]
        n = len(arr)
        print(Solution.minOperations(arr, n))
