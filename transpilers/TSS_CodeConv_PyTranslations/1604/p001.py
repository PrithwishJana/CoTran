import math

class p001:
    @staticmethod
    def main(args):
        print((p001()).run())
    def run(self):
        sum = 0
        for i in range(0, 1000):
            if math.fmod(i, 3) == 0 or math.fmod(i, 5) == 0:
                sum += i
        return str(sum)
