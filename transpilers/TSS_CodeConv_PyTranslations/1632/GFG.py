class GFG:
    @staticmethod
    def minimumCostOfBreaking(X, Y, m, n):
        res = 0
        java.util.Arrays.sort(X, java.util.Collections.reverseOrder())
        java.util.Arrays.sort(Y, java.util.Collections.reverseOrder())
        hzntl = 1
        vert = 1
        i = 0
        j = 0
        while i < m and j < n:
            if X [i] > Y [j]:
                res += X [i] * vert
                hzntl += 1
                i += 1
            else:
                res += Y [j] * hzntl
                vert += 1
                j += 1
        total = 0
        while i < m:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: total += X [i ++];
            total += X [i ]
            i += 1
        res += total * vert
        total = 0
        while j < n:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: total += Y [j ++];
            total += Y [j ]
            j += 1
        res += total * hzntl
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        m = 6
        n = 4
        X = [2, 1, 3, 1, 4]
        Y = [4, 1, 2]
        print(GFG.minimumCostOfBreaking(X, Y, m - 1, n - 1), end = '')
