import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(n):
        sum = 0
        i = 1
        while i <= math.sqrt(n):
            if math.fmod(n, i) == 0:
                if math.trunc(n / float(i)) == i:
                    sum = sum + i
                else:
                    sum = sum + i
                    sum = sum + (math.trunc(n / float(i)))
            i += 1
        return sum - n
    @staticmethod
    def printAliquot(n):
        print("{0:d} ".format(n), end = '')
        s = TreeSet()
        s.add(n)
        next = 0
        while n > 0:
            n = GFG.getSum(n)
            if s.contains(n) and n != s.last():
                print("\nRepeats with " + str(n), end = '')
                break
            print(str(n) + " ", end = '')
            s.add(n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.printAliquot(12)
