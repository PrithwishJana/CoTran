import math

class IS:
    @staticmethod
    def main(args):
        (IS()).runapp()
    def runapp(self):
        scan = java.util.Scanner(System.in)
        n = scan.nextInt()
        d = scan.nextInt()
        sequence = [0 for _ in range(n)]
        step = 0
        store = 0
        for x in range(0, n):
            sequence [x] = scan.nextInt()
        y = 0
        while y < n - 1:
            while sequence [y + 1] <= sequence [y]:
                diff = sequence [y + 1] - sequence [y]
                if sequence [y + 1] == sequence [y]:
                    sequence [y + 1] = sequence [y + 1] + d
                    step = step + 1
                else:
                    diff = - diff
                    store = (math.trunc(diff / float(d))) + 1
                    step = step + store
                    sequence [y + 1] = sequence [y + 1] + (d * store)
            y += 1
        print("{0:d}".format(step), end = '')
