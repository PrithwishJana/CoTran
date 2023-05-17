import math

class _424A:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        sc.nextLine()
        s = sc.nextLine()
        sittingToStanding = 0
        sitting = 0
        standing = 0
        for i in range(0, n):
            if s[i] == 'x':
                sitting += 1
            else:
                standing += 1
        sittingToStanding = math.trunc((sitting - standing) / float(2))
        print(abs(sittingToStanding))
        for i in range(0, n):
            if s[i] == 'x' and sittingToStanding > 0:
                print('X', end = '')
                sittingToStanding -= 1
            elif s[i] == 'X' and sittingToStanding < 0:
                print('x', end = '')
                sittingToStanding += 1
            else:
                print(s[i], end = '')
