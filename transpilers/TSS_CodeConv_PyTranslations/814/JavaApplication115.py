class JavaApplication115:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        num = sc.nextInt()
        arr = []
        arra = []
        maxdif = 0
        maxAll = 1000000000
        for i in range(0, num):
            h = sc.nextInt()
            arr.append(h)
            arra.append(h)
        i = 1
        while i < num - 1:
            j = 0
            while j < len(arr) - 1:
                if j == i:
                    maxdif = max(abs(arr[j - 1] - arr[j + 1]), maxdif)
                else:
                    maxdif = max(abs(arr[j] - arr[j + 1]), maxdif)
                j += 1
            maxAll = min(maxAll, maxdif)
            maxdif = 0
            i += 1
        print(maxAll)
