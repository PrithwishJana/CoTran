import math

class GFG:
    @staticmethod
    def findFrequencyUtil(arr, low, high, freq):
        if arr [low] == arr [high]:
            freq [arr [low]] += high - low + 1
        else:
            mid = math.trunc((low + high) / float(2))
            GFG.findFrequencyUtil(arr, low, mid, freq)
            GFG.findFrequencyUtil(arr, mid + 1, high, freq)
    @staticmethod
    def findFrequency(arr, n):
        freq = [0 for _ in range(arr [n - 1] + 1)]
        GFG.findFrequencyUtil(arr, 0, n - 1, freq)
        i = 0
        while i <= arr [n - 1]:
            if freq [i] != 0:
                print("Element " + str(i) + " occurs " + str(freq [i]) + " times")
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10]
        n = len(arr)
        GFG.findFrequency(arr, n)
