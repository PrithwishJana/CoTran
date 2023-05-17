class GFG:
    CHARS = 26
    @staticmethod
    def isValidString(str):
        freq = [0 for _ in range(GFG.CHARS)]
        i = 0
        while i < len(str):
            freq [str[i] - 'a'] += 1
            i += 1
        i = 0
        freq1 = 0
        count_freq1 = 0
        i = 0
        while i < GFG.CHARS:
            if freq [i] != 0:
                freq1 = freq [i]
                count_freq1 = 1
                break
            i += 1
        j = 0
        freq2 = 0
        count_freq2 = 0
        j = i + 1
        while j < GFG.CHARS:
            if freq [j] != 0:
                if freq [j] == freq1:
                    count_freq1 += 1
                else:
                    count_freq2 = 1
                    freq2 = freq [j]
                    break
            j += 1
        k = j + 1
        while k < GFG.CHARS:
            if freq [k] != 0:
                if freq [k] == freq1:
                    count_freq1 += 1
                if freq [k] == freq2:
                    count_freq2 += 1
                else:
                    return False
            if count_freq1 > 1 and count_freq2 > 1:
                return False
            k += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "abcbc"
        if GFG.isValidString(str):
            print("YES")
        else:
            print("NO")
