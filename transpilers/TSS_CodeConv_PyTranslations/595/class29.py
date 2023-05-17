import math

class class29:
    @staticmethod
    def main(arg):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = sc.nextInt()
            st = HashSet()
            i = 0
            flag = 0
            a = [0 for _ in range(n)]
            vis = [0 for _ in range(n)]
            for i in range(0, n):
                a [i] = sc.nextInt()
                val = math.fmod((i + a [i]), n)
                if val < 0:
                    val += n
                vis [int(val)] = 1
            for i in range(0, n):
                if vis [i] == 0:
                    flag = 1
                    break
            if flag == 0:
                print("YES")
            else:
                print("NO")
        t -= 1
