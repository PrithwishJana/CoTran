import math

class A1642:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        T = in_.nextInt()
        for t in range(0, T):
            X = [0 for _ in range(3)]
            Y = [0 for _ in range(3)]
            for i in range(0, 3):
                X [i] = in_.nextInt()
                Y [i] = in_.nextInt()
            answer = 0
            for i in range(0, 3):
                if Y [i] == Y [math.fmod((i + 1), 3)] and Y [i] > Y [math.fmod((i + 2), 3)]:
                    answer += abs(X [math.fmod((i + 1), 3)] - X [i])
            print(answer)
