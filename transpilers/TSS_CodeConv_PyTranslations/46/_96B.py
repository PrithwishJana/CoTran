class _96B:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        number = in_.nextLong()
        ans = - 1
        value = 0
        mask = 2
        while value < number:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: String s = Integer.toBinaryString(mask ++).substring(1);
            s = Integer.toBinaryString(mask ).substring(1)
            mask += 1
            zeros = 0
            for c in s.toCharArray():
                if c == '0':
                    zeros += 1
            if zeros != len(s) - zeros:
                continue
            s = s.replace('0', '4')
            s = s.replace('1', '7')
            value = int(s)
        print(value)
