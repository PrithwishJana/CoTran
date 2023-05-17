import math

class main:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scn = Scanner(System.in)
        n = scn.nextInt()
        k = scn.nextInt()
        i = 1
        req = 1
        while k - req >= 0:
            if k - req >= 0:
                k = k - req
            else:
                break
            i += 1
            if math.fmod(i, n) != 0:
                req = math.fmod(i, n)
            else:
                req = n
        print(k)
