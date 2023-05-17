import math

class solution:
    @staticmethod
    def minimumX(n, k):
        mini = Integer.MAX_VALUE
        i = 1
        while i * i <= n:
            if math.fmod(n, i) == 0:
                fir = i
                sec = math.trunc(n / float(i))
                num1 = fir * k + sec
                res = (math.trunc(num1 / float(k))) * (math.fmod(num1, k))
                if res == n:
                    mini = min(num1, mini)
                num2 = sec * k + fir
                res = (math.trunc(num2 / float(k))) * (math.fmod(num2, k))
                if res == n:
                    mini = min(num2, mini)
            i += 1
        return mini
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        k = 6
        print(solution.minimumX(n, k))
        n = 5
        k = 5
        print(solution.minimumX(n, k))
