class StroneGame:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        t = sc.nextInt()
        while t > 0:
            n = sc.nextInt()
            ar = [0 for _ in range(n)]
            max = 0
            min = 100000
            x = 0
            y = 0
            for i in range(0, n):
                ar [i] = sc.nextInt()
                if ar [i] < min:
                    min = ar [i]
                    x = i + 1
                if ar [i] > max:
                    max = ar [i]
                    y = i + 1
            pos1 = 0
            pos2 = 1
            pos3 = 0
            pos4 = 1
            a = 0
            b = 0
            mm = 0
            total = 0
            pos1 = x
            pos2 += n - x
            if pos1 < pos2:
                a = pos1
            else:
                a = pos2
            pos3 = y
            pos4 += n - y
            if pos3 < pos4:
                b = pos3
            else:
                b = pos4
            div = abs(y - x)
            if div < a or div < b:
                mm = min(a, b)
                total += mm + div
            else:
                total += a + b
            print(total)
            t -= 1
