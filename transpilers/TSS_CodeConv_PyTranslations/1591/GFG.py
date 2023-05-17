import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(N):
        isPrime = True
        arr = [7, 11, 13, 17, 19, 23, 29, 31]
        if N < 2:
            isPrime = False
        if math.fmod(N, 2) == 0 or math.fmod(N, 3) == 0 or math.fmod(N, 5) == 0:
            isPrime = False
        i = 0
        while i < math.sqrt(N):
            for c in arr:
                if c > math.sqrt(N):
                    break
                else:
                    if math.fmod(N, (c + i)) == 0:
                        isPrime = False
                        break
                if not isPrime:
                    break
            i += 30
        if isPrime:
            print("Prime Number")
        else:
            print("Not a Prime Number")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 121
        GFG.isPrime(N)
