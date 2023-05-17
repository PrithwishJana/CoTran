class p024:
    @staticmethod
    def main(args):
        print((p024()).run())
    def run(self):
        array = [0 for _ in range(10)]
        i = 0
        while i < len(array):
            array [i] = i
            i += 1
        for i in range(0, 999999):
            if not Library.nextPermutation(array):
                raise AssertionError()
        ans = ""
        i = 0
        while i < len(array):
            ans += array [i]
            i += 1
        return ans
