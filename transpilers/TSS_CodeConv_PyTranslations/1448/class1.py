import math

class class1:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        input = Scanner(System.in)
        t = input.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            n = input.nextLong()
            ans = 0
            flag = 0
            while n > 0:
                x = 0
                if math.fmod(n, 2) == 0:
                    temp = math.trunc(n / float(2))
                    if math.fmod(n, 4) == 0 and n > 8:
                        temp = n - 1
                        x += 1
                    n = temp
                    if flag == 0:
                        flag = 1
                        if x > 0:
                            ans += 1
                        else:
                            ans += temp
                    else:
                        flag = 0
                else:
                    if flag == 0:
                        n = n - 1
                        ans += 1
                        flag = 1
                    else:
                        n = n - 1
                        flag = 0
            print(ans)
        t -= 1
