import math

class B272:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        stat = [0 for _ in range(30)]
        for n in range(0, N):
            a = in_.nextInt()
            stat [Integer.bitCount(a)] += 1
        answer = 0
        for count in stat:
            answer += count * (count - 1)
        answer = math.trunc(answer / float(2))
        print(answer)
