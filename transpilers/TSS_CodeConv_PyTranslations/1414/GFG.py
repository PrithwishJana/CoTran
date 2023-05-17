class GFG:
    @staticmethod
    def CountTrailingZeros(n):
        bit = Integer.toBinaryString(n)
        bit1 = StringBuilder()
        bit1.append(bit)
        bit1 = bit1.reverse()
        zero = 0
        for i in range(0, 64):
            if bit1.charAt(i) == '0':
                zero += 1
            else:
                break
        return zero
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        ans = GFG.CountTrailingZeros(n)
        print(ans)
