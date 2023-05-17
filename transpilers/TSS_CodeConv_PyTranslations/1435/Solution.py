import math

class Solution:
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
            sum = 0
            for i in range(0, n):
                a [i] = sc.nextLong()
                sum += a [i]
            if math.fmod(sum, n) != 0:
                print("NO")
            else:
                sum = math.trunc(sum / float(n))
                flag = False
                for i in range(0, n):
                    if a [i] == sum:
                        flag = True
                        break
                if flag:
                    print("YES")
                else:
                    print("NO")
        t -= 1
