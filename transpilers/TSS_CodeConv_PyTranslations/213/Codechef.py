class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        try:
            sc = Scanner(System.in)
            t = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
            while t  > 0:
                t -= 1
                a = sc.nextInt()
                b = sc.nextInt()
                x = sc.nextInt()
                y = sc.nextInt()
                ans = max(max(x, a - 1 - x) * b, a * max(y, b - 1 - y))
                print(ans)
            t -= 1
        except Exception as e:
            pass
