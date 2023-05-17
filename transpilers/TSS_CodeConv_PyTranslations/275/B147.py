class B147:
    @staticmethod
    def main(args):
        scanner = Scanner(System.in)
        n = scanner.nextInt()
        c = [0 for _ in range(n)]
        table = [[0 for _ in range(50)] for _ in range(50)]
        for i in range(0, n):
            c [i] = scanner.nextInt()
        map = {}
        for i in range(1, n + 1):
            j = 1
            while j <= c [i - 1]:
                cell = scanner.nextInt()
                map[cell] = Point(i, j)
                table [i - 1][j - 1] = cell
                j += 1
        cnt = 0
        m = 0
        sb = StringBuilder()
        for i in range(0, n):
            j = 0
            while j < c [i]:
                cnt += 1
                if table [i][j] == cnt:
                    j += 1
                    continue
                sb.append(i + 1).append(" ")
                sb.append(j + 1).append(" ")
                point = map[cnt]
                sb.append(point.x).append(" ")
                sb.append(point.y).append("\n")
                tmp = table [i][j]
                table [i][j] = table [point.x - 1][point.y - 1]
                table [point.x - 1][point.y - 1] = tmp
                map[tmp] = point
                m += 1
                j += 1
        print(m)
        s = str(sb)
        if m > 0:
            print(s)
class Point:
    def __init__(self, x, y):
        #instance fields found by Java to Python Converter:
        self.x = 0
        self.y = 0

        self.x = x
        self.y = y
