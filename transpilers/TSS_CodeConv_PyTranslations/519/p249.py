import math

class p249:
    @staticmethod
    def main(args):
        print((p249()).run())
    _LIMIT = 5000
    _MODULUS = 10000000000000000
    def run(self):
        isPrime = Library.listPrimality(math.trunc(p249._LIMIT * p249._LIMIT / float(2)))
        numSubsets = [0 for _ in range(math.trunc(p249._LIMIT * p249._LIMIT / float(2)))]
        numSubsets [0] = 1
        maxSum = 0
        for i in range(0, p249._LIMIT):
            if not isPrime [i]:
                continue
            maxSum += i
            for j in range(maxSum, i - 1, -1):
                temp = numSubsets [j] + numSubsets [j - i]
                if temp < p249._MODULUS:
                    numSubsets [j] = temp
                else:
                    numSubsets [j] = temp - p249._MODULUS
        sum = 0
        i = 0
        while i < len(numSubsets):
            if isPrime [i]:
                sum = math.fmod((sum + numSubsets [i]), p249._MODULUS)
            i += 1
        return str(sum)
