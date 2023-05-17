import math

class GFG:
    @staticmethod
    def countOccurrences(x, d):
        count = 0
        while x > 0:
            if math.fmod(x, 10) == d:
                count += 1
            x = math.trunc(x / float(10))
        return count
    @staticmethod
    def maxOccurring(x):
        if x < 0:
            x = - x
        result = 0
        max_count = 1
        for d in range(0, 10):
            count = GFG.countOccurrences(x, d)
            if count >= max_count:
                max_count = count
                result = d
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 1223355
        print("Max occurring digit is " + str(GFG.maxOccurring(x)))
