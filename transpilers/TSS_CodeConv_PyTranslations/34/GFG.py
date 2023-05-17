import math

class GFG:
    @staticmethod
    def lehmann(n, t):
        rand = java.util.Random()
        a = rand.nextInt(n - 3) + 2
        e = math.trunc((n - 1) / float(2))
        while t > 0:
            result = math.fmod((int((a ** e))), n)
            if (math.fmod(result, n)) == 1 or (math.fmod(result, n)) == (n - 1):
                a = rand.nextInt(n - 3) + 2
                t -= 1
            else:
                return - 1
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 13
        t = 10
        if n == 2:
            print(" 2 is Prime.")
        if math.fmod(n, 2) == 0:
            print(str(n) + " is Composite")
        else:
            flag = GFG.lehmann(n, t)
            if flag == 1:
                print(str(n) + " may be Prime.")
            else:
                print(str(n) + " is Composite.")
