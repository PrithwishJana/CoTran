class GFG:
    @staticmethod
    def mostFrequent(arr, n):
        Arrays.sort(arr)
        max_count = 1
        res = arr [0]
        curr_count = 1
        for i in range(1, n):
            if arr [i] == arr [i - 1]:
                curr_count += 1
            else:
                if curr_count > max_count:
                    max_count = curr_count
                    res = arr [i - 1]
                curr_count = 1
        if curr_count > max_count:
            max_count = curr_count
            res = arr [n - 1]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 5, 2, 1, 3, 2, 1]
        n = len(arr)
        print(GFG.mostFrequent(arr, n))
