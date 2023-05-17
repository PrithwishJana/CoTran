class GFG:
    @staticmethod
    def printKMissing(arr, n, k):
        arr.sort()
        i = 0
        while i < n and arr [i] <= 0:
            i += 1
        count = 0
        curr = 1
        while count < k and i < n:
            if arr [i] != curr:
                print(str(curr) + " ", end = '')
                count += 1
            else:
                i += 1
            curr += 1
        while count < k:
            print(str(curr) + " ", end = '')
            curr += 1
            count += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4]
        n = len(arr)
        k = 3
        GFG.printKMissing(arr, n, k)
