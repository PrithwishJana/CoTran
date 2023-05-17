import math

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
                a = sc.nextLong()
                b = sc.nextLong()
                if a < b:
                    print(b - a)
                else:
                    if math.fmod(a, 2) != math.fmod(b, 2):
                        print(1)
                    else:
                        print(0)
            t -= 1
        except Exception as e:
            pass
