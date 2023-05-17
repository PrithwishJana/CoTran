class FastFoodRestaurant:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        test = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (test -- > 0)
        while test  > 0:
            test -= 1
            a = sc.nextInt()
            b = sc.nextInt()
            c = sc.nextInt()
            if a == 0 and b == 0 and c == 0:
                print(0)
            else:
                if b > c and b > a:
                    k = a
                    a = b
                    b = k
                if c > b and c > a:
                    k = a
                    a = c
                    c = k
                res = 0
                if a >= 1:
                    a -= 1
                    res += 1
                if b >= 1:
                    b -= 1
                    res += 1
                if c >= 1:
                    c -= 1
                    res += 1
                if a >= 1 and b >= 1:
                    a -= 1
                    b -= 1
                    res += 1
                if a >= 1 and c >= 1:
                    a -= 1
                    c -= 1
                    res += 1
                if c >= 1 and b >= 1:
                    c -= 1
                    b -= 1
                    res += 1
                if a >= 1 and b >= 1 and c >= 1:
                    res += 1
                print(res)
        test -= 1
