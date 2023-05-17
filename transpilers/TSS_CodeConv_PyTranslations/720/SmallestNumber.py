class SmallestNumber:
    min = 0
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        SmallestNumber.min = Long.MAX_VALUE
        arr = []
        for i in range(0, 4):
            arr.append(sc.nextLong())
        ops = [None for _ in range(3)]
        for i in range(0, 3):
            ops [i] = sc.next()
        SmallestNumber.util(arr, ops, 0)
        print(SmallestNumber.min)
    @staticmethod
    def util(arr, ops, idx):
        if idx == 3:
            SmallestNumber.min = min(SmallestNumber.min, arr[0])
            return
        for i, unusedItem in enumerate(arr):
            for j in range(i + 1, len(arr)):
                a = []
                for k, unusedItem in enumerate(arr):
                    if k != j and k != i:
                        a.append(arr[k])
                res = 0
                if idx < 3 and ops [idx] == "+":
                    res = arr[i] + arr[j]
                else:
                    res = arr[i] * arr[j]
                a.append(res)
                SmallestNumber.util(a, ops, idx + 1)
