class GFG:
    @staticmethod
    def maxsum_SIS(arr, n):
        max_sum = 0
        current_sum = arr [0]
        for i in range(1, n):
            if arr [i - 1] < arr [i]:
                current_sum = current_sum + arr [i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = arr [i]
        return max(max_sum, current_sum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 2, 4]
        n = len(arr)
        print("Maximum sum : " + str(GFG.maxsum_SIS(arr, n)))
