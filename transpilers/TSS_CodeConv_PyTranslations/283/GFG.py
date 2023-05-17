import math

class GFG:
    N = 1000
    @staticmethod
    def lastElement(a, n):
        steps = 1
        v = [None for _ in range(GFG.N)]
        i = 0
        while i < GFG.N:
            v [i] = list  ()
            i += 1
        if n == 1:
            return a [0]
        for i in range(0, n, 2):
            v [steps].append(a [i] | a [i + 1])
        while len(v[steps])) > 1:
            steps += 1
            for i in range(0, len(v[steps - 1])), 2):
                if math.fmod(steps, 2) == 1:
                    v [steps].append(v [steps - 1].get(i) | v [steps - 1].get(i + 1))
                else:
                    v [steps].append(v [steps - 1].get(i) ^ v [steps - 1].get(i + 1))
        return v [steps].get(0)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 4, 5, 6]
        n = len(a)
        index = 0
        value = 2
        a [0] = 2
        print(GFG.lastElement(a, n))
        index = 3
        value = 5
        a [index] = value
        print(GFG.lastElement(a, n))
