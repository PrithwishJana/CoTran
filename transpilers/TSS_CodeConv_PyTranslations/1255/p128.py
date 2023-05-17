class p128:
    @staticmethod
    def main(args):
        print((p128()).run())
    _TARGET = 2000
    def run(self):
        count = 2
        ring = 2
        while True:
            if int(ring) * 12 + 5 > Integer.MAX_VALUE:
                raise ArithmeticException()
            if Library.isPrime(ring * 6 - 1) and Library.isPrime(ring * 6 + 1) and Library.isPrime(ring * 12 + 5):
                count += 1
                if count == p128._TARGET:
                    return str(int(ring) * (ring - 1) * 3 + 2)
            if Library.isPrime(ring * 6 - 1) and Library.isPrime(ring * 6 + 5) and Library.isPrime(ring * 12 - 7):
                count += 1
                if count == p128._TARGET:
                    return str(int(ring) * (ring + 1) * 3 + 1)
            ring += 1
