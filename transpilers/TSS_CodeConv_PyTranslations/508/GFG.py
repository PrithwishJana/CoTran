class GFG:
    @staticmethod
    def lis(arr, n):
        max = 0
        lst = [0 for _ in range(n)]
        Arrays.fill(lst, 1)
        for i in range(1, n):
            for j in range(0, i):
                if arr [i] > arr [j] and lst [i] < lst [j] + 1:
                    lst [i] = lst [j] + 1
        for i in range(0, n):
            if max < lst [i]:
                max = lst [i]
        return max
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 22, 9, 33, 21, 50, 41, 60]
        n = len(arr)
        print("Length of lst is " + str(GFG.lis(arr, n)))
