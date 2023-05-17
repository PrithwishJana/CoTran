class GFG:
    @staticmethod
    def maxDiff(arr, n):
        diff = arr [1] - arr [0]
        curr_sum = diff
        max_sum = curr_sum
        i = 1
        while i < n - 1:
            diff = arr [i + 1] - arr [i]
            if curr_sum > 0:
                curr_sum += diff
            else:
                curr_sum = diff
            if curr_sum > max_sum:
                max_sum = curr_sum
            i += 1
        return max_sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [80, 2, 6, 3, 100]
        n = len(arr)
        print("Maximum difference is " + str(GFG.maxDiff(arr, n)), end = '')
