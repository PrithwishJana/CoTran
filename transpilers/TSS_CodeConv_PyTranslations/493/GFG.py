class GFG:
    @staticmethod
    def minimumSwaps(arr):
        count = 0
        i = 0
        while i < len(arr):
            if arr [i] != i + 1:
                while arr [i] != i + 1:
                    temp = 0
                    temp = arr [arr [i] - 1]
                    arr [arr [i] - 1] = arr [i]
                    arr [i] = temp
                    count += 1
            i += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 1, 5]
        print(GFG.minimumSwaps(arr))
