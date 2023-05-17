import math

class GFG:
    @staticmethod
    def count_even_odd(min, max, steps):
        a = 0
        b = 0
        even = 0
        odd = 0
        beven = True
        aeven = False
        n = 2
        for i in range(0, n):
            a = steps [i][0]
            b = steps [i][1]
            if not(aeven or (a & 1) > 0):
                aeven = True
            if beven:
                if (b & 1) > 0:
                    beven = False
            elif not((a & 1) > 0):
                if not((b & 1) > 0):
                    beven = True
            else:
                if (b & 1) > 0:
                    beven = True
        if beven:
            even = math.trunc(int(max) / float(2)) - math.trunc(int((min - 1)) / float(2))
            odd = 0
        else:
            even = math.trunc(int(max) / float(2)) - math.trunc(int((min - 1)) / float(2))
            odd = 0
        if not(beven ^ aeven):
            even += max - min + 1 - math.trunc(int(max) / float(2)) + math.trunc(int((min - 1)) / float(2))
        else:
            odd += max - min + 1 - math.trunc(int(max) / float(2)) + math.trunc(int((min - 1)) / float(2))
        print("even = " + str(even) + ", odd = " + str(odd))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        min = 1
        max = 4
        steps = [[ 1, 2 ], [ 3, 4 ]]
        GFG.count_even_odd(min, max, steps)
