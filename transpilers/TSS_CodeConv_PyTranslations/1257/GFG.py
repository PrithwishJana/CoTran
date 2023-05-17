import math

class GFG:
    @staticmethod
    def Digits(n):
        largest = 0
        smallest = 9
        while n != 0:
            r = math.fmod(n, 10)
            largest = max(r, largest)
            smallest = min(r, smallest)
            n = math.trunc(n / float(10))
        print(str(largest) + " " + str(smallest))
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2346
        GFG.Digits(n)
