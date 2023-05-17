class GFG:
    @staticmethod
    def minimumChanges(arr, n, d):
        maxFreq = - 1
        freq = {}
        for i in range(0, n):
            a0 = arr [i] - (i) * d
            if a0 in freq.keys():
                freq[a0] = freq[a0] + 1
            else:
                freq[a0] = 1
            if freq[a0] > maxFreq:
                maxFreq = freq[a0]
        return (n - maxFreq)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        d = 1
        arr = [1, 3, 3, 4, 6]
        print(GFG.minimumChanges(arr, n, d))
