class GFG:
    @staticmethod
    def LongestFibSubseq(A, n):
        S = TreeSet()
        for t in A:
            S.add(t)
        maxLen = 0
        x = 0
        y = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                x = A [j]
                y = A [i] + A [j]
                length = 3
                while S.contains(y) and (y != S.last()):
                    z = x + y
                    x = y
                    y = z
                    length += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: maxLen = Math.max(maxLen, ++ length);
                    maxLen = max(maxLen,  length)
        return maxLen if maxLen >= 3 else 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        n = len(A)
        print(GFG.LongestFibSubseq(A, n), end = '')
