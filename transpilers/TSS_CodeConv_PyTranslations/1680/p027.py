class p027:
    @staticmethod
    def main(args):
        print((p027()).run())
    def run(self):
        bestNum = 0
        bestA = 0
        bestB = 0
        for a in range(- 1000, 1001):
            for b in range(- 1000, 1001):
                num = p027._numberOfConsecutivePrimesGenerated(a, b)
                if num > bestNum:
                    bestNum = num
                    bestA = a
                    bestB = b
        return str(bestA * bestB)
    @staticmethod
    def _numberOfConsecutivePrimesGenerated(a, b):
        i = 0
        while True:
            n = i * i + i * a + b
            if n < 0 or not Library.isPrime(n):
                return i
            i += 1
