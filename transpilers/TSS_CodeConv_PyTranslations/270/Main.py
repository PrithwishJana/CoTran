class geeksforgeeks:
    @staticmethod
    def minOperations(ar, k):
        ar.sort()
        opsNeeded = 0
        for i in range(0, k):
            opsNeeded += ar [k - 1] - ar [i]
        ans = opsNeeded
        i = k
        while i < len(ar):
            opsNeeded = opsNeeded - (ar [i - 1] - ar [i - k])
            opsNeeded += (k - 1) * (ar [i] - ar [i - 1])
            ans = min(ans, opsNeeded)
            i += 1
        return ans
    @staticmethod
    def main(args):
        arr = [3, 1, 9, 100]
        n = len(arr)
        k = 3
        print(geeksforgeeks.minOperations(arr, k))
