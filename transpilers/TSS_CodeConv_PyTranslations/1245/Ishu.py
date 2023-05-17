class Ishu:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        scan = java.util.Scanner(System.in)
        i = 0
        j = 0
        x = 0
        y = 0
        k = 0
        dx = 0
        dy = 0
        flag = True
        s = None
        ch = ['\0' for _ in range(100)]
        co = [[0 for _ in range(101)] for _ in range(2)]
        s = scan.next()
        ch = s.toCharArray()
        co [0][k] = x
        co [1][k] = y
        k += 1
        i = 0
        while i < len(s):
            if ch [i] == 'L':
                x -= 1
            elif ch [i] == 'R':
                x += 1
            elif ch [i] == 'U':
                y += 1
            elif ch [i] == 'D':
                y -= 1
            co [0][k] = x
            co [1][k] = y
            k += 1
            i += 1
        i = 0
        while i < k - 3:
            for j in range(i + 3, k):
                dx = co [0][i] - co [0][j]
                dy = co [1][i] - co [1][j]
                if dx < 0:
                    dx *= (- 1)
                if dy < 0:
                    dy *= (- 1)
                if (dx <= 1 and dy == 0) or (dy <= 1 and dx == 0):
                    flag = False
                    break
            if not flag:
                break
            i += 1
        if flag:
            print("OK")
        else:
            print("BUG")
