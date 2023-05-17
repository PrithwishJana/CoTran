class p179:
    @staticmethod
    def main(args):
        print((p179()).run())
    _LIMIT = Library.pow(10, 7)
    def run(self):
        numDivisors = [0 for _ in range(p179._LIMIT + 1)]
        Arrays.fill(numDivisors, 2)
        i = 2
        while i < len(numDivisors):
            j = i * 2
            while j < len(numDivisors):
                numDivisors [j] += 1
                j += i
            i += 1
        count = 0
        i = 2
        while i < len(numDivisors) - 1:
            if numDivisors [i] == numDivisors [i + 1]:
                count += 1
            i += 1
        return str(count)
