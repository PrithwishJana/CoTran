import math

class GFG:
    MAX = 100005
    @staticmethod
    def addPrimes():
        n = GFG.MAX
        prime = [False for _ in range(n + 1)]
        Arrays.fill(prime, True)
        p = 2
        while p * p <= n:
            if prime [p] == True:
                for i in range(p * p, n + 1, p):
                    prime [i] = False
            p += 1
        ans = list  ()
        for p in range(2, n + 1):
            if prime [p]:
                ans.append(p)
        return ans
    @staticmethod
    def is_prime(n):
        return (n == 3 or n == 5 or n == 7)
    @staticmethod
    def find_Sum(n):
        sum = 0
        v = GFG.addPrimes()
        i = 0
        while i < len(v) and n > 0:
            flag = 1
            a = v[i]
            while a != 0:
                d = math.fmod(a, 10)
                a = math.trunc(a / float(10))
                if GFG.is_prime(d):
                    flag = 0
                    break
            if flag == 1:
                n -= 1
                sum = sum + v[i]
            i += 1
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        print(GFG.find_Sum(n))
