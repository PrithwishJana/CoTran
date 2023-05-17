import math

class GrowTheTree:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        nums = [0 for _ in range(n)]
        for i in range(0, n):
            nums [i] = sc.nextInt()
        nums.sort()
        firstHalf = 0
        secondHalf = 0
        length = math.trunc(n / float(2))
        for i in range(0, length):
            firstHalf += nums [i]
        for i in range(length, n):
            secondHalf += nums [i]
        result = (firstHalf * firstHalf) + (secondHalf * secondHalf)
        print(result)
