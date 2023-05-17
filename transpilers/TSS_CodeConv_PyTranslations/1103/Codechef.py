class Codechef:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        try:
            sc = Scanner(System.in)
            n = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (n -- > 0)
            while n  > 0:
                n -= 1
                e = sc.nextInt()
                s = sc.nextInt()
                t = sc.nextInt()
                temp = max(e - s, e - t)
                print(temp + 1)
            n -= 1
        except Exception as e:
            pass
