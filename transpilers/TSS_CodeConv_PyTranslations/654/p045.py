import math

class p045:
    @staticmethod
    def main(args):
        print((p045()).run())
    def run(self):
        i = 286
        j = 166
        k = 144
        while True:
            triangle = math.trunc(int(i) * (i + 1) / float(2))
            pentagon = math.trunc(int(j) * (j * 3 - 1) / float(2))
            hexagon = int(k) * (k * 2 - 1)
            min = min(min(triangle, pentagon), hexagon)
            if min == triangle and min == pentagon and min == hexagon:
                return str(min)
            if min == triangle:
                i += 1
            if min == pentagon:
                j += 1
            if min == hexagon:
                k += 1
