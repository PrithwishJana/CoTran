class MaximumDiffrence:
    def maxDiff(self, arr, arr_size):
        max_diff = arr [1] - arr [0]
        min_element = arr [0]
        i = 0
        for i in range(1, arr_size):
            if arr [i] - min_element > max_diff:
                max_diff = arr [i] - min_element
            if arr [i] < min_element:
                min_element = arr [i]
        return max_diff
    @staticmethod
    def main(args):
        maxdif = MaximumDiffrence()
        arr = [1, 2, 6, 80, 100]
        size = len(arr)
        print("Maximum difference is " + str(maxdif.maxDiff(arr, size)))
