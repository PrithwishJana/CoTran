class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxPrimefactorNum(N):
        arr = [False for _ in range(N + 5)]
        i = 3
        while i * i <= N:
            if not arr [i]:
                for j in range(i * i, N + 1, i):
                    arr [j] = True
            i += 2
        prime = []
        prime.insert(len(prime), 2)
        for i in range(3, N + 1, 2):
            if not arr [i]:
                prime.insert(len(prime), i)
        i = 0
        ans = 1
        while ans * prime[i] <= N and i < len(prime):
            ans *= prime[i]
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 40
        print(GFG.maxPrimefactorNum(N))
