class Problem5:
    @staticmethod
    def main(args):
        input = Scanner(System.in)
        n1 = input.nextInt()
        arr = [0 for _ in range(n1)]
        sum = 0
        for i in range(0, n1):
            n2 = input.nextInt()
            arr [i] = n2
            sum += float(arr [i])
        summ = sum
        summ /= float(n1)
        nos = 0
        i = 0
        while i < len(arr):
            if arr [i] == summ:
                nos += 1
            i += 1
        print(nos)
        for i in range(0, n1):
            if float(arr [i]) == summ:
                print(str(i + 1) + " ", end = '')
