import math

class Good_seq:
    sc = Scanner(System.in)
    pw = java.io.PrintWriter(System.out)
    dp = [0 for _ in range(100001)]
    @staticmethod
    def factoriseopt(n):
        ans = []
        if n == 1:
            ans.append(1)
            return ans
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                cnt = 0
                while math.fmod(n, i) == 0:
                    cnt += 1
                    n = math.trunc(n / float(i))
                ans.append(i)
            i += 1
        if n != 1:
            ans.append(n)
        return ans
    @staticmethod
    def main(args):
        n = Good_seq.sc.nextInt()
        arr = [0 for _ in range(n)]
        for i in range(0, n):
            arr [i] = Good_seq.sc.nextInt()
        for i in range(0, n):
            ansArrayList = Good_seq.factoriseopt(arr [i])
            best = 0
            for x in ansArrayList:
                best = max(best, Good_seq.dp [x])
            for x in ansArrayList:
                Good_seq.dp [x] = best + 1
        maxsofar = 0
        for x in Good_seq.dp:
            maxsofar = max(maxsofar, x)
        print(maxsofar)
