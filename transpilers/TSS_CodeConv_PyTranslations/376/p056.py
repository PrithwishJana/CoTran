class p056:
    @staticmethod
    def main(args):
        print((p056()).run())
    def run(self):
        max = 0
        for a in range(1, 100):
            for b in range(1, 100):
                pow = java.math.BigInteger.valueOf(a).pow(b)
                max = max(p056._digitSum(pow), max)
        return str(max)
    @staticmethod
    def _digitSum(n):
        sum = 0
        s = str(n)
        i = 0
        while i < len(s):
            sum += s[i] - '0'
            i += 1
        return sum
