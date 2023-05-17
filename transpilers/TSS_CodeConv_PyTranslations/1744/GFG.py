import math

class GFG:
    @staticmethod
    def findKthChar(s, k):
        len = len(s)
        i = 0
        total_len = 0
        while i < len:
#JAVA TO PYTHON CONVERTER WARNING: Java 'isLetter' is not identical to Python 'isalpha' (review Java and Python documentation):
#ORIGINAL LINE: if (Character.isLetter(s.charAt(i)))
            if (s[i]).isalpha():
                total_len += 1
                if total_len == k:
                    return s[i]
                i += 1
            else:
                n = 0
#JAVA TO PYTHON CONVERTER WARNING: Java 'isLetter' is not identical to Python 'isalpha' (review Java and Python documentation):
#ORIGINAL LINE: while (i < len && ! Character.isLetter(s.charAt(i)))
                while i < len and not (s[i]).isalpha():
                    n = n * 10 + (s[i] - '0')
                    i += 1
                next_total_len = total_len * n
                if k <= next_total_len:
                    pos = math.fmod(k, total_len)
                    if pos == 0:
                        pos = total_len
                    return GFG.findKthChar(s, pos)
                else:
                    total_len = next_total_len
        return ' '
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "ab2c3"
        k = 5
        print(GFG.findKthChar(s, k))
