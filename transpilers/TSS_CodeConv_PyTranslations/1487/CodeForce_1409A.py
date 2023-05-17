import math

class CodeForce_1409A:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        t = scanner.nextInt()
        a = 0
        b = 0
        for i in range(0, t):
            a = scanner.nextInt()
            b = scanner.nextInt()
            counter = 0
            if a < b:
                counter = math.trunc((b - a) / float(10))
            elif a > b:
                counter = math.trunc((a - b) / float(10))
            if math.fmod(a, 10) != math.fmod(b, 10):
                counter += 1
            print(counter)
