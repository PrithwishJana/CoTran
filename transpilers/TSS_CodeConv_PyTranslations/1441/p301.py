class p301:
    @staticmethod
    def main(args):
        print((p301()).run())
    def run(self):
        a = 0
        b = 1
        for i in range(0, 32):
            c = a + b
            a = b
            b = c
        return str(a)
