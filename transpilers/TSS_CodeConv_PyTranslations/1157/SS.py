import math

class SS:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        n = in_.nextInt()
        b = in_.nextInt()
        arr = [0 for _ in range(n)]
        v = []
        odd = 0
        even = 0
        count = 0
        i = 0
        while i < len(arr):
            arr [i] = in_.nextInt()
            i += 1
        i = 0
        while i < len(arr):
            if i != 0 and odd == even:
                v.append(abs(arr [i] - arr [i - 1]))
            if math.fmod(arr [i], 2) == 0:
                even += 1
            else:
                odd += 1
            i += 1
        v.sort()
        for i, unusedItem in enumerate(v):
            if b >= v[i]:
                count += 1
                b -= v[i]
        print(count)
