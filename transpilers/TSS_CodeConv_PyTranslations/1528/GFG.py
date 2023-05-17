class GFG:
    @staticmethod
    def Count_subarray(arr, n):
        subarray_sum = 0
        remaining_sum = 0
        count = 0
        for i in range(0, n):
            for j in range(i, n):
                subarray_sum = 0
                remaining_sum = 0
                for k in range(i, j + 1):
                    subarray_sum += arr [k]
                for l in range(0, i):
                    remaining_sum += arr [l]
                for l in range(j + 1, n):
                    remaining_sum += arr [l]
                if subarray_sum > remaining_sum:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 9, 12, 6]
        n = len(arr)
        print(GFG.Count_subarray(arr, n), end = '')
