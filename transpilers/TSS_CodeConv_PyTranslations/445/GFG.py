import math

class GFG:
    @staticmethod
    def msb(x):
        ret = 0
        while (x >> (ret + 1)) != 0:
            ret += 1
        return ret
    @staticmethod
    def xorRange(l, r):
        max_bit = GFG.msb(r)
        mul = 2
        ans = 0
        for i in range(1, max_bit + 1):
            if (math.trunc(l / float(mul))) * mul == (math.trunc(r / float(mul))) * mul:
                if ((l & (1 << i)) != 0) and math.fmod((r - l + 1), 2) == 1:
                    ans += mul
                mul *= 2
                continue
            odd_c = 0
            if ((l & (1 << i)) != 0) and math.fmod(l, 2) == 1:
                odd_c = (odd_c ^ 1)
            if ((r & (1 << i)) != 0) and math.fmod(r, 2) == 0:
                odd_c = (odd_c ^ 1)
            if odd_c != 0:
                ans += mul
            mul *= 2
        zero_bit_cnt = zero_bit_cnt = math.trunc((r - l + 1) / float(2))
        if math.fmod(l, 2) == 1 and math.fmod(r, 2) == 1:
            zero_bit_cnt += 1
        if math.fmod(zero_bit_cnt, 2) == 1:
            ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 1
        r = 4
        print(GFG.xorRange(l, r), end = '')
