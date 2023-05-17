import math

class PolandBoardAndGame:
    sc = java.util.Scanner(System.in)
    @staticmethod
    def main(args):
        n = PolandBoardAndGame.sc.nextInt()
        m = PolandBoardAndGame.sc.nextInt()
        if n > m:
            print("YES")
        elif m > n:
            print("NO")
        else:
            map = {}
            for i in range(0, n):
                map[PolandBoardAndGame.sc.next()] = 1
            dem = 0
            for i in range(0, m):
                if PolandBoardAndGame.sc.next() in map.keys():
                    dem += 1
            if math.fmod(dem, 2) == 0:
                print("NO")
            else:
                print("YES")
