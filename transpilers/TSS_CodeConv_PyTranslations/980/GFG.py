class GFG:
    @staticmethod
    def FindRank(arr, length):
        print("1" + " ", end = '')
        i = 1
        while i < len(arr):
            rank = 1
            for j in range(0, i):
                if arr [j] > arr [i]:
                    rank += 1
            print(str(rank) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [88, 14, 69, 30, 29, 89]
        len = len(arr)
        GFG.FindRank(arr, len)
