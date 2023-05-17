class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(a, b, n):
        ans = [0 for _ in range(n)]
        max = Integer.MIN_VALUE
        for i in range(0, n):
            max = max(max, (a [i] - b [i]))
        if max < 0:
            return False
        for i in range(0, n):
            temp = a [i] - max
            if temp <= 0:
                ans [i] = 0
            else:
                ans [i] = temp
        for i in range(0, n):
            if ans [i] != b [i]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            a = [0 for _ in range(n)]
            b = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = sc.nextInt()
            for i in range(0, n):
                b [i] = sc.nextInt()
            if Solution.solve(a, b, n) == True:
                print("YES")
            else:
                print("NO")
        t -= 1
