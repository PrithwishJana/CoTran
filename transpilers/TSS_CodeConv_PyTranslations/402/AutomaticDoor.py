import math

class AutomaticDoor:
    @staticmethod
    def main(args):
        scan = Scanner(System.in)
        n = scan.nextLong()
        m = scan.nextInt()
        a = scan.nextLong()
        d = scan.nextLong()
        arr = [0 for _ in range(m)]
        for i in range(0, m):
            arr [i] = scan.nextLong()
        count = 0
        time = 0
        x = math.trunc(d / float(a)) + 1
        y = d - (x - 1) * a
        if y < 0:
            y = 0
        last = 0
        i = 0
        while i < m:
            b = max(min(math.trunc((arr [i] - 1) / float(a)), n), 0)
            c = b - time
            k = math.trunc(c / float(x))
            count += k
            time += k * x
            if k != 0:
                while i < m and arr [i] <= time * a + y:
                    i += 1
            if i >= m:
                break
            count += 1
            last = arr [i] + d
            if time < n:
                last = min(last, (time + 1) * a + d)
            while i < m and arr [i] <= last:
                i += 1
            time = max(time, min(n, math.trunc(last / float(a))))
        if time < n:
            count += math.trunc((n - time + x - 1) / float(x))
        print(count)
