import math

class Test1:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        list = []
        x = sc.nextLong()
        while x > 0:
            r = math.fmod(x, 10)
            if 9 - r < r:
                if math.trunc(x / float(10)) == 0 and 9 - r == 0:
                    list.append(r)
                else:
                    list.append(9 - r)
            else:
                list.append(r)
            x = math.trunc(x / float(10))
        pow = 0
        newNumber = 0
        for i, unusedItem in enumerate(list):
            newNumber = newNumber + list[i] * int(10) ** pow
            pow += 1
        print(newNumber)
