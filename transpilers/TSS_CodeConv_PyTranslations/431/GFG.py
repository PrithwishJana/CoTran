class GFG:
    @staticmethod
    def getPrime(arr, n):
        max_val = Arrays.stream(arr).max().getAsInt()
        prime = list(max_val + 1)
        i = 0
        while i < max_val + 1:
            prime.insert(i, True)
            i += 1
        prime.insert(1, False)
        prime.insert(2, False)
        p = 2
        while p * p <= max_val:
            if prime[p] == True:
                for i in range(p * 2, max_val + 1, p):
                    prime.insert(i, False)
            p += 1
        maximum = - 1
        for i in range(0, n):
            if prime[arr [i]]:
                maximum = max(maximum, arr [i])
        return maximum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 10, 15, 7, 6, 8, 13]
        n = len(arr)
        print(GFG.getPrime(arr, n))
