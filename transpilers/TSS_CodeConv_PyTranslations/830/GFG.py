class GFG:
    @staticmethod
    def findMaxValue(arr, n):
        if n < 4:
            print("The array should have" + " atleast 4 elements")
        table1 = [0 for _ in range(n + 1)]
        table2 = [0 for _ in range(n)]
        table3 = [0 for _ in range(n - 1)]
        table4 = [0 for _ in range(n - 2)]
        Arrays.fill(table1, Integer.MIN_VALUE)
        Arrays.fill(table2, Integer.MIN_VALUE)
        Arrays.fill(table3, Integer.MIN_VALUE)
        Arrays.fill(table4, Integer.MIN_VALUE)
        for i in range(n - 1, -1, -1):
            table1 [i] = max(table1 [i + 1], arr [i])
        for i in range(n - 2, -1, -1):
            table2 [i] = max(table2 [i + 1], table1 [i + 1] - arr [i])
        for i in range(n - 3, -1, -1):
            table3 [i] = max(table3 [i + 1], table2 [i + 1] + arr [i])
        for i in range(n - 4, -1, -1):
            table4 [i] = max(table4 [i + 1], table3 [i + 1] - arr [i])
        return table4 [0]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 8, 9, 2, 20]
        n = len(arr)
        print(GFG.findMaxValue(arr, n))
