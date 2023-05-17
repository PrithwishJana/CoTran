import math

class CandyAndFriend:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
        while t > 0:
            n = sc.nextInt()
            a = [0 for _ in range(n)]
            sum = 0
            count = 0
            for i in range(0, n):
                a [i] = sc.nextInt()
                sum += a [i]
            if math.fmod(sum, n) == 0:
                div = math.trunc(sum / float(n))
                for i in range(0, n):
                    if a [i] > div:
                        count += 1
                print(count)
            else:
                print(- 1)
            t -= 1
