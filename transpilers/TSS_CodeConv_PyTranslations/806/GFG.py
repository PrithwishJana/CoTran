class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxZeros(n):
        if n == 0 or (n & (n - 1)) == 0:
            return - 1
        b = 4
        setBit = 1
        prev = 0
        i = 0
        i = 1
        while i <= b * 8:
            prev += 1
            if (n & setBit) == setBit:
                setBit = setBit << 1
                break
            setBit = setBit << 1
            i += 1
        max0 = Integer.MIN_VALUE
        cur = prev
        j = i + 1
        while j <= b * 8:
            cur += 1
            if (n & setBit) == setBit:
                if max0 < (cur - prev - 1):
                    max0 = cur - prev - 1
                prev = cur
            setBit = setBit << 1
            j += 1
        return max0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 549
        print(GFG.maxZeros(n))
