class Main1:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        m = sc.nextInt()
        pic = [['\0' for _ in range(m)] for _ in range(n)]
        temp = None
        for i in range(0, n):
            temp = sc.next()
            for j in range(0, m):
                pic [i][j] = temp[j]
        inc = 0
        inc1 = 0
        comeIn = [False for _ in range(4)]
        if n > 1 or m > 1:
            x = 0
            while x < n - 1:
                y = 0
                while y < m - 1:
                    i = x
                    while i < 2 + x:
                        j = y
                        while j < 2 + y:
                            if pic [i][j] == 'f' and comeIn [0] == False:
                                inc += 1
                                comeIn [0] = True
                            elif pic [i][j] == 'a' and comeIn [1] == False:
                                inc += 1
                                comeIn [1] = True
                            elif pic [i][j] == 'c' and comeIn [2] == False:
                                inc += 1
                                comeIn [2] = True
                            elif pic [i][j] == 'e' and comeIn [3] == False:
                                inc += 1
                                comeIn [3] = True
                            j += 1
                        i += 1
                    if inc == 4:
                        inc1 += 1
                    inc = 0
                    Arrays.fill(comeIn, False)
                    y += 1
                x += 1
            print(inc1)
        else:
            print("0")
        sc.close()
