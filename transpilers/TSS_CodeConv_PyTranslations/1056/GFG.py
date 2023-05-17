class GFG:
    @staticmethod
    def maxPartitions(arr, n):
        ans = 0
        max_so_far = 0
        for i in range(0, n):
            max_so_far = max(max_so_far, arr [i])
            if max_so_far == i:
                ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 0, 2, 3, 4]
        n = len(arr)
        print(GFG.maxPartitions(arr, n))
