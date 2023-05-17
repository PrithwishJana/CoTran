import math

class Ideone:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
    def main(args):
        sc = Scanner(System.in)
        n = int(sc.nextLine())
        for i in range(0, n):
            sum = - int(sc.nextLine())
            for x in sc.nextLine().trim().split(" "):
                sum += int(x)
            if math.fmod(sum, 2) == 0:
                print("maomao90")
            else:
                print("errorgorn")
