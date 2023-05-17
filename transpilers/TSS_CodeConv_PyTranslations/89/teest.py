import math

class teest(java.io.PrintWriter):
    def __init__(self):
        super().__init__(System.out)
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] $) throws java.io.IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main($):
        o = teest()
        o.main()
        o.flush()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: void main() throws java.io.IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(self):
        a = Scanner(System.in)
        t = a.nextInt()
        while t > 0:
            n = a.nextInt()
            k = a.nextInt()
            if math.fmod(n, 2) != math.fmod(k, 2) or math.trunc(n / float(k)) < k:
                print("NO")
            else:
                print("YES")
            t -= 1
