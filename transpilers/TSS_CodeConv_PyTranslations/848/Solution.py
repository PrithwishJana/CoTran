class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(agrs):
        sc = Scanner(System.in)
        out = PrintWriter(System.out)
        n = sc.nextInt()
        a = [0 for _ in range(n)]
        b = [0 for _ in range(n)]
        total = 0
        for i in range(0, n):
            a [i] = sc.nextInt()
            b [i] = sc.nextFloat()
            total += b [i] / 2.0
        dp = [[0 for _ in range(10001)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            Arrays.fill(dp [i], - 1)
        dp [0][0] = total
        for i in range(0, n):
            for k in range(n - 1, -1, -1):
                for j in range(0, 10001):
                    if dp [k][j] == - 1:
                        continue
                    dp [k + 1][j + a [i]] = float(max(dp [k + 1][j + a [i]], dp [k][j] + b [i] / 2.0))
        max = 0
        for k in range(1, n + 1):
            max = 0
            for j in range(0, 10001):
                max = float(max(max, min(dp [k][j], j)))
            out.print(str(max) + " ")
        out.flush()
