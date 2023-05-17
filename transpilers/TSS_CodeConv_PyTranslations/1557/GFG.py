import math

class GFG:
    @staticmethod
    def LongestSubarray(arr, n, k):
        arr2 = [0 for _ in range(n)]
        for i in range(0, n):
            arr2 [i] = math.fmod(arr [i], k)
        current_length = 0
        max_length = 0
        j = 0
        i = 0
        while i < n:
            current_length = 1
            for j in range(i + 1, n):
                if arr2 [j] == arr2 [i]:
                    current_length += 1
                else:
                    break
            max_length = max(max_length, current_length)
            i = j
        return max_length
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 9, 7, 18, 29, 11]
        n = len(arr)
        k = 11
        print(GFG.LongestSubarray(arr, n, k))
