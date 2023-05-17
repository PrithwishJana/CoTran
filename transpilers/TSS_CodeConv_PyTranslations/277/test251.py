class test251:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        t = in_.nextInt()
        for i in range(0, t):
            a = in_.next().toCharArray()
            if len(a) >= 3:
                z = 0
                o = 0
                j = 0
                while j < len(a):
                    if a [j] == '1':
                        o += 1
                    else:
                        z += 1
                    j += 1
                if z > o:
                    print(o)
                elif o > z:
                    print(z)
                else:
                    print(z - 1)
            else:
                print(0)
        in_.close()
