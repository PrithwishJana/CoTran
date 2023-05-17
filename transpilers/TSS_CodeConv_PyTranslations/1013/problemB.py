import math

class problemB:
    @staticmethod
    def quickSort(a, d, c):
        i = d
        j = c
        mid = a [math.trunc((d + c) / float(2))]
        while i <= j:
            while a [i] < mid:
                i += 1
            while a [j] > mid:
                j -= 1
            if i <= j:
                tg = a [i]
                a [i] = a [j]
                a [j] = tg
                i += 1
                j -= 1
        if d < j:
            problemB.quickSort(a, d, j)
        if i < c:
            problemB.quickSort(a, i, c)
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = sc.nextInt()
        a = [0 for _ in range(n + 5)]
        for i in range(1, n + 1):
            a [i] = sc.nextInt()
        b = [0 for _ in range(n + 5)]
        for i in range(1, n):
            b [i] = sc.nextInt()
        c = [0 for _ in range(n + 5)]
        i = 1
        while i <= n - 2:
            c [i] = sc.nextInt()
            i += 1
        problemB.quickSort(a, 1, n)
        problemB.quickSort(b, 1, n - 1)
        problemB.quickSort(c, 1, n - 2)
        resA = a [n]
        for i in range(1, n):
            if a [i] != b [i]:
                resA = a [i]
                break
        print(resA)
        resB = b [n - 1]
        i = 1
        while i <= n - 2:
            if b [i] != c [i]:
                resB = b [i]
                break
            i += 1
        print(resB)
        sc.close()
