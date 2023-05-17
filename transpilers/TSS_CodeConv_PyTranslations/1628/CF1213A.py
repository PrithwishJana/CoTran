import math

class CF1213A:
    @staticmethod
    def main(args):
        scan = java.util.Scanner(System.in)
        n = scan.nextInt()
        even = 0
        odd = 0
        for i in range(0, n):
            num1 = scan.nextInt()
            if math.fmod(num1, 2) == 0:
                even += 1
            else:
                odd += 1
        if even > odd:
            print(odd)
        else:
            print(even)
