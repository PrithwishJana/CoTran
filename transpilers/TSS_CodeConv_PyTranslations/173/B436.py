import math

class B436:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        M = in_.nextInt()
        in_.nextInt()
        answer = [0 for _ in range(M)]
        for n in range(0, N):
            S = in_.next().toCharArray()
            for m in range(0, M):
                c = S [m]
                if c == 'L':
                    hit = m - n
                    if hit >= 0:
                        answer [hit] += 1
                elif c == 'R':
                    hit = m + n
                    if hit < M:
                        answer [hit] += 1
                elif c == 'U':
                    if math.fmod(n, 2) == 0:
                        answer [m] += 1
        output = StringBuilder()
        for a in answer:
            output.append(a).append(' ')
        print(output)
