import math

class B975:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        a = [0 for _ in range(14)]
        for i in range(0, 14):
            a [i] = sc.nextInt()
        max = 0
        for from_ in range(0, 14):
            stones = a [from_]
            remainder = math.trunc(stones / float(14))
            score = remainder if (math.fmod(remainder, 2) == 0) else 0
            for i in range(1, 14):
                count = a [math.fmod((from_ + i), 14)] + math.trunc((stones + 14 - i) / float(14))
                if math.fmod(count, 2) == 0:
                    score += count
            max = max(max, score)
        print(max)
