import math

class GFG:
    class Date:
        def __init__(self, d, m, y):
            #instance fields found by Java to Python Converter:
            self.d = 0
            self.m = 0
            self.y = 0

            self.d = d
            self.m = m
            self.y = y
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    @staticmethod
    def countLeapYears(d):
        years = d.y
        if d.m <= 2:
            years -= 1
        return math.trunc(years / float(4)) - math.trunc(years / float(100)) + math.trunc(years / float(400))
    @staticmethod
    def getDifference(dt1, dt2):
        n1 = dt1.y * 365 + dt1.d
        i = 0
        while i < dt1.m - 1:
            n1 += GFG.monthDays [i]
            i += 1
        n1 += GFG.countLeapYears(dt1)
        n2 = dt2.y * 365 + dt2.d
        i = 0
        while i < dt2.m - 1:
            n2 += GFG.monthDays [i]
            i += 1
        n2 += GFG.countLeapYears(dt2)
        return (n2 - n1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        dt1 = Date(1, 2, 2000)
        dt2 = Date(1, 2, 2004)
        print("Difference between two dates is " + str(GFG.getDifference(dt1, dt2)))
