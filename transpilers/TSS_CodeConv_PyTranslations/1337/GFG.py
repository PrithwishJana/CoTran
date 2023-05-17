class GFG:
    @staticmethod
    def findMinDel(arr, n):
        min_num = Integer.MAX_VALUE
        for i in range(0, n):
            min_num = min(arr [i], min_num)
        cnt = 0
        for i in range(0, n):
            if arr [i] == min_num:
                cnt += 1
        return n - cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 3, 2]
        n = len(arr)
        print(GFG.findMinDel(arr, n), end = '')
