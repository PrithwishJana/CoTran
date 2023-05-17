class GFG:
    @staticmethod
    def maxdiff(arr, n):
        freq = {}
        for i in range(0, n):
            freq[arr [i]] = 1 if freq[arr [i]] is None else freq[arr [i]] + 1
        ans = 0
        for i in range(0, n):
            for j in range(0, n):
                if freq[arr [i]] > freq[arr [j]] and arr [i] > arr [j]:
                    ans = max(ans, freq[arr [i]] - freq[arr [j]])
                elif freq[arr [i]] < freq[arr [j]] and arr [i] < arr [j]:
                    ans = max(ans, freq[arr [j]] - freq[arr [i]])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 1, 3, 2, 3, 2]
        n = len(arr)
        print(GFG.maxdiff(arr, n))
