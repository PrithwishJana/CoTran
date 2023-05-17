class FlippingGame:
    @staticmethod
    def main(args):
        scanner = java.util.Scanner(System.in)
        if scanner.hasNext():
            n = scanner.nextInt()
            arr = [0 for _ in range(n)]
            for i in range(0, n):
                arr [i] = scanner.nextInt()
            max = Integer.MIN_VALUE
            for i in range(0, n):
                for j in range(i, n):
                    x = 0
                    brr = [0 for _ in range(n)]
                    for k in arr:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: brr [x ++] = k;
                        brr [x ] = k
                        x += 1
                    for k in range(i, j + 1):
                        if brr [k] == 0:
                            brr [k] = 1
                        else:
                            brr [k] = 0
                    count = FlippingGame._checKNo(brr)
                    if count > max:
                        max = count
            if n == 1:
                if arr [0] == 1:
                    print(0)
                else:
                    print(1)
            else:
                print(max)
    @staticmethod
    def _checKNo(brr):
        val = 0
        for i in brr:
            if i == 1:
                val += 1
        return val
