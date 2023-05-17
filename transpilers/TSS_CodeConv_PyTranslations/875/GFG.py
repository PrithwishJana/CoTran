class GFG:
    @staticmethod
    def indexedSequentialSearch(arr, n, k):
        elements = [0 for _ in range(20)]
        indices = [0 for _ in range(20)]
        temp = 0
        i = 0
        j = 0
        ind = 0
        start = 0
        end = 0
        for i in range(0, n, 3):
            elements [ind] = arr [i]
            indices [ind] = i
            ind += 1
        if k < elements [0]:
            print("Not found")
            return
        else:
            for i in range(1, ind + 1):
                if k < elements [i]:
                    start = indices [i - 1]
                    end = indices [i]
                    break
        for i in range(start, end + 1):
            if k == arr [i]:
                j = 1
                break
        if j == 1:
            print("Found at index " + str(i))
        else:
            print("Not found")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [6, 7, 8, 9, 10]
        n = len(arr)
        k = 8
        GFG.indexedSequentialSearch(arr, n, k)
