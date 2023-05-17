import math

class VasyaTheHipster:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        a = 0
        b = 0
        a = sc.nextInt()
        b = sc.nextInt()
        count = 0
        while True:
            if a > 0 and b > 0:
                count += 1
                a -= 1
                b -= 1
            else:
                break
        ans = math.trunc(a / float(2)) + math.trunc(b / float(2))
        print(str(count) + " " + str(ans))
