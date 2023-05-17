class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countFreq(a, n):
        hm = [0 for _ in range(n)]
        for i in range(0, n):
            hm [a [i]] += 1
        cumul = 0
        for i in range(0, n):
            cumul += hm [a [i]]
            if hm [a [i]] != 0:
                print(str(a [i]) + "->" + str(cumul))
            hm [a [i]] = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 3, 2, 4, 2, 1]
        n = len(a)
        GFG.countFreq(a, n)
