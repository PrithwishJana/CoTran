class GFG:
    @staticmethod
    def frequencyOfSmallest(n, arr):
        mn = arr [0]
        freq = 1
        for i in range(1, n):
            if arr [i] < mn:
                mn = arr [i]
                freq = 1
            elif arr [i] == mn:
                freq += 1
        return freq
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 5
        arr = [3, 2, 3, 4, 4]
        print(GFG.frequencyOfSmallest(N, arr))
