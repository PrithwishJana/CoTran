class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countTriplets(arr, n, m):
        count = 0
        Arrays.sort(arr)
        end = 0
        start = 0
        mid = 0
        for end in range(n - 1, 1, -1):
            start = 0
            mid = end - 1
            while start < mid:
                prod = arr [end] * arr [start] * arr [mid]
                if prod > m:
                    mid -= 1
                elif prod < m:
                    start += 1
                elif prod == m:
                    count += 1
                    mid -= 1
                    start += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 1, 1, 1, 1]
        n = len(arr)
        m = 1
        print(GFG.countTriplets(arr, n, m))
