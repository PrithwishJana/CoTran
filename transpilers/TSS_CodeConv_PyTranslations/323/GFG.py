class GFG:
    @staticmethod
    def find3Numbers(arr, n):
        small = + 2147483647
        large = + 2147483647
        i = 0
        for i in range(0, n):
            if arr [i] <= small:
                small = arr [i]
            elif arr [i] <= large:
                large = arr [i]
            else:
                break
        if i == n:
            print("No such triplet found")
            return
        for j in range(0, i + 1):
            if arr [j] < large:
                small = arr [j]
                break
        print(str(small) + " " + str(large) + " " + str(arr [i]))
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        arr = [5, 7, 4, 8]
        n = len(arr)
        GFG.find3Numbers(arr, n)
