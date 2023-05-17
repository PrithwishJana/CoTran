class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return GFG.__gcd(a - b, b)
        return GFG.__gcd(a, b - a)
    @staticmethod
    def Probability(sum, times):
        favorable = 0
        total = 36
        probability = 0
        for i in range(1, 7):
            for j in range(1, 7):
                if (i + j) == sum:
                    favorable += 1
        gcd1 = GFG.__gcd(int(favorable), int(total))
        favorable = favorable / float(gcd1)
        total = total / float(gcd1)
        probability = int(total) ** times
        return probability
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sum = 7
        times = 7
        print("1" + "/" + str(GFG.Probability(sum, times)))
