class GFG:
    @staticmethod
    def FindMinNumber(arr, n, k):
        i = 0
        j = 0
        min_num = Integer.MAX_VALUE
        found = False
        sum = 0
        while i < n:
            sum = sum + arr [i]
            if sum == k:
                min_num = min(min_num, ((n - (i + 1)) + j))
                found = True
            elif sum > k:
                while sum > k:
                    sum = sum - arr [j]
                    j += 1
                if sum == k:
                    min_num = min(min_num, ((n - (i + 1)) + j))
                    found = True
            i += 1
        if found:
            return min_num
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 3, 2, 5, 6]
        n = len(arr)
        k = 5
        print(GFG.FindMinNumber(arr, n, k))
