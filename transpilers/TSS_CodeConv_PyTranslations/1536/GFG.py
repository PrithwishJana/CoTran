import math

class GFG:
    @staticmethod
    def pythagoreanTriplet(n):
        i = 1
        while i <= math.trunc(n / float(3)):
            j = i + 1
            while j <= math.trunc(n / float(2)):
                k = n - i - j
                if i * i + j * j == k * k:
                    print(str(i) + ", " + str(j) + ", " + str(k), end = '')
                    return
                j += 1
            i += 1
        print("No Triplet", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        n = 12
        GFG.pythagoreanTriplet(n)
