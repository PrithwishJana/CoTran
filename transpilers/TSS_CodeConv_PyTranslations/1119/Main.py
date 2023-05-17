class OddOccurance:
    def getOddOccurrence(self, ar, ar_size):
        i = 0
        res = 0
        for i in range(0, ar_size):
            res = res ^ ar [i]
        return res
    @staticmethod
    def main(args):
        occur = OddOccurance()
        ar = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
        n = len(ar)
        print(occur.getOddOccurrence(ar, n))
