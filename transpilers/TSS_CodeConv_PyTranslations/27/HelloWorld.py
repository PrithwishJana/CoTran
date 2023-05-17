class HelloWorld:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- != 0)
        while t  != 0:
            t -= 1
            n = sc.nextInt()
            sb = StringBuilder()
            if n == 1:
                print(3)
            else:
                while n > 0:
                    ans = n & 1
                    n = n >> 1
                    if ans == 1:
                        sb.insert(0, 1)
                        break
                    else:
                        sb.insert(0, 0)
                if n == 0:
                    sb.deleteCharAt(sb.length() - 1)
                    sb.append(1)
                val = Integer.parseInt(str(sb), 2)
                print(val)
        t -= 1
