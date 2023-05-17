class GFG:
    @staticmethod
    def FindSubarray(arr, n, k):
        count_one = [0 for _ in range(n)]
        for i in range(0, n):
            count_one [i] = Integer.bitCount(arr [i])
        sum = count_one [0]
        if n == 1:
            if count_one [0] >= k:
                return 1
            else:
                return - 1
        ans = Integer.MAX_VALUE
        i = 1
        j = 0
        while i < n:
            if k == count_one [j]:
                ans = 1
                break
            elif k == count_one [i]:
                ans = 1
                break
            elif sum + count_one [i] < k:
                sum += count_one [i]
                i += 1
            elif sum + count_one [i] > k:
                ans = min(ans, (i - j) + 1)
                sum -= count_one [j]
                j += 1
            elif sum + count_one [i] == k:
                ans = min(ans, (i - j) + 1)
                sum += count_one [i]
                i += 1
        if ans != Integer.MAX_VALUE:
            return ans
        else:
            return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 4, 8]
        n = len(arr)
        k = 2
        print(GFG.FindSubarray(arr, n, k))
