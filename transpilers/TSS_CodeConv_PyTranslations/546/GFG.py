import math

class GFG:
    @staticmethod
    def nondecdigits(n):
        x = 0
        for x in range(n, 0, -1):
            no = x
            prev_dig = 11
            flag = True
            while no != 0:
                if prev_dig < math.fmod(no, 10):
                    flag = False
                    break
                prev_dig = math.fmod(no, 10)
                no = math.trunc(no / float(10))
            if flag == True:
                break
        return x
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 200
        print(GFG.nondecdigits(n))
