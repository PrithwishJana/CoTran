import math

class HelloWorld:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scanner = Scanner(System.in)
        num = scanner.nextInt()
        pairs = [[0 for _ in range(2)] for _ in range(num)]
        for i in range(0, num):
            pairs [i][0] = scanner.nextLong()
            pairs [i][1] = scanner.nextLong()
        commonFactors = HashSet()
        for i in range(0, 2):
            X = pairs [0][i]
            k = 2
            while k <= int(math.ceil(math.sqrt(X))):
                if math.fmod(X, k) == 0:
                    while math.fmod(X, k) == 0:
                        X = math.trunc(X / float(k))
                    commonFactors.add(k)
                k += 1
            if X != 1:
                commonFactors.add(X)
        for val in commonFactors:
            works = True
            i = 0
            while i < len(pairs):
                if math.fmod(pairs [i][0], val) > 0 and math.fmod(pairs [i][1], val) > 0:
                    works = False
                    break
                i += 1
            if works:
                print(val)
                return
        print(- 1)
