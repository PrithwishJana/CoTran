import math

class GFG:
    @staticmethod
    def pairCount(arr, n):
        max_val = Arrays.stream(arr).max().getAsInt()
        prime = list(max_val + 1)
        i = 0
        while i < max_val + 1:
            prime.append(True)
            i += 1
        prime.insert(0, False)
        prime.insert(1, False)
        p = 2
        while p * p <= max_val:
            if prime[p] == True:
                for i in range(p * 2, max_val + 1, p):
                    prime.insert(i, False)
            p += 1
        count = 0
        for i in range(0, n):
            if prime[arr [i]]:
                count += 1
        return math.trunc((count * (count - 1)) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5, 6, 7]
        n = len(arr)
        print(GFG.pairCount(arr, n))
