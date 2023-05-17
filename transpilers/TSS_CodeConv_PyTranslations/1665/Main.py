class Binary:
    @staticmethod
    def maxOnesIndex(arr, n):
        max_count = 0
        max_index = 0
        prev_zero = - 1
        prev_prev_zero = - 1
        for curr in range(0, n):
            if arr [curr] == 0:
                if curr - prev_prev_zero > max_count:
                    max_count = curr - prev_prev_zero
                    max_index = prev_zero
                prev_prev_zero = prev_zero
                prev_zero = curr
        if n - prev_prev_zero > max_count:
            max_index = prev_zero
        return max_index
    @staticmethod
    def main(args):
        arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        n = len(arr)
        print("Index of 0 to be replaced is " + str(Binary.maxOnesIndex(arr, n)))
