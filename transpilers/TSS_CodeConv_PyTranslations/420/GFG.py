import math

class GFG:
    @staticmethod
    def normalSieve(n):
        prime = [False for _ in range(math.trunc(n / float(2)))]
        Arrays.fill(prime, False)
        i = 3
        while i * i < n:
            if prime [math.trunc(i / float(2))] == False:
                for j in range(i * i, n, i * 2):
                    prime [math.trunc(j / float(2))] = True
            i += 2
        print("2 ", end = '')
        for i in range(3, n, 2):
            if prime [math.trunc(i / float(2))] == False:
                print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 100
        GFG.normalSieve(n)
