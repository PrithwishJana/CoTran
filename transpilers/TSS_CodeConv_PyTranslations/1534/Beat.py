import math

class Beat:
    def __init__(self, number):
        #instance fields found by Java to Python Converter:
        self.number = 0

        self.number = number
    def getNumber(self):
        return self.number
    numberEven = 0
    numberOdd = 0
    def input(self, number):
        if math.fmod(number, 2) == 0:
            Beat.numberEven += 1
        else:
            Beat.numberOdd += 1
    def printResult(self):
        print(min(Beat.numberEven, Beat.numberOdd))
        Beat.numberEven = 0
        Beat.numberOdd = 0
    @staticmethod
    def main(a):
        input = java.util.Scanner(System.in)
        number = input.nextInt()
        instance = Beat(number)
        i = 0
        while i < instance.getNumber():
            num = input.nextInt()
            for k in range(0, num):
                n = input.nextInt()
                instance.input(n)
            instance.printResult()
            i += 1
