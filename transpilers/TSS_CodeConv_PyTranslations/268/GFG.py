import math

class GFG:
    @staticmethod
    def find_Centroid(v):
        ans = [0 for _ in range(2)]
        n = len(v)
        signedArea = 0
        for i in range(0, n):
            x0 = v [i][0]
            y0 = v [i][1]
            x1 = v [math.fmod((i + 1), n)][0]
            y1 = v [math.fmod((i + 1), n)][1]
            A = (x0 * y1) - (x1 * y0)
            signedArea += A
            ans [0] += (x0 + x1) * A
            ans [1] += (y0 + y1) * A
        signedArea *= 0.5
        ans [0] = (ans [0]) / (6 * signedArea)
        ans [1] = (ans [1]) / (6 * signedArea)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        vp = [[ 1, 2 ], [ 3, - 4 ], [ 6, - 7 ]]
        ans = GFG.find_Centroid(vp)
        print("{0:.3f}".format(ans [0]) + " " + "{0:.3f}".format(ans [1]))
