class GFG:
    @staticmethod
    def minimumAdjacentDifference(a, n, k):
        minDiff = Integer.MAX_VALUE
        i = 0
        while i < (1 << n):
            cnt = Integer.bitCount(i)
            if cnt == n - k:
                temp = list  ()
                for j in range(0, n):
                    if (i & (1 << j)) != 0:
                        temp.append(a [j])
                maxDiff = Integer.MIN_VALUE
                j = 0
                while j < len(temp) - 1:
                    maxDiff = max(maxDiff, temp[j + 1] - temp[j])
                    j += 1
                minDiff = min(minDiff, maxDiff)
            i += 1
        return minDiff
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 2
        a = [3, 7, 8, 10, 14]
        print(GFG.minimumAdjacentDifference(a, n, k))
