class GFG:
    @staticmethod
    def Solution(A):
        ans = 2
        n = len(A)
        if n <= 2:
            return n
        llap = [0 for _ in range(n)]
        for i in range(0, n):
            llap [i] = 2
        Arrays.sort(A)
        for j in range(n - 2, -1, -1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < n:
                if A [i] + A [k] == 2 * A [j]:
                    llap [j] = max(llap [k] + 1, llap [j])
                    ans = max(ans, llap [j])
                    i -= 1
                    k += 1
                elif A [i] + A [k] < 2 * A [j]:
                    k += 1
                else:
                    i -= 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [9, 4, 7, 2, 10]
        print(str(GFG.Solution(a)) + "\n", end = '')
