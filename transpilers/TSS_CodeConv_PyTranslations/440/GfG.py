class GfG:
    SIZE = 26
    @staticmethod
    def longSubstring(str1, k):
        freq = [0 for _ in range(GfG.SIZE)]
        str = str1.toCharArray()
        start = 0
        maxLen = 0
        ch = '\0'
        n = len(str1)
        for i in range(0, n):
            ch = str [i]
            freq [ch - 'a'] += 1
            if freq [ch - 'a'] > k:
                if maxLen < (i - start):
                    maxLen = i - start
                while freq [ch - 'a'] > k:
                    freq [str [start] - 'a'] -= 1
                    start += 1
        if maxLen < (n - start):
            maxLen = n - start
        return maxLen
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        str = "babcaag"
        k = 1
        print("Length = " + str(GfG.longSubstring(str, k)))
