class PellNumber:
    @staticmethod
    def pell(n):
        if n <= 2:
            return n
        return 2 * PellNumber.pell(n - 1) + PellNumber.pell(n - 2)
    @staticmethod
    def main(args):
        n = 4
        print(PellNumber.pell(n))
