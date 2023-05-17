class GFG:
    @staticmethod
    def isSubArray(A, B, n, m):
        i = 0
        j = 0
        while i < n and j < m:
            if A [i] == B [j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                i = i - j + 1
                j = 0
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        A = [2, 3, 0, 5, 1, 1, 2]
        n = len(A)
        B = [3, 0, 5, 1]
        m = len(B)
        if GFG.isSubArray(A, B, n, m):
            print("YES")
        else:
            print("NO")
