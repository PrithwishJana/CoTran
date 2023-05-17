class CodeForces1389B:
    @staticmethod
    def main(args):
        input = Scanner(System.in)
        t = input.nextInt()
        for i in range(0, t):
            n = input.nextInt()
            k = input.nextInt()
            z = input.nextInt()
            a = [0 for _ in range(n)]
            for j in range(0, n):
                a [j] = input.nextInt()
            res = 0
            for zz in range(0, z + 1):
                dist = k - 2 * zz
                if dist < 0:
                    break
                max = 0
                score = 0
                for j in range(0, dist + 1):
                    if j < n - 1:
                        max = max(max, a [j] + a [j + 1])
                    score += a [j]
                res = max(res, score + max * zz)
            print(res)
