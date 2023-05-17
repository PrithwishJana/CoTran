class GFG:
    @staticmethod
    def longestString(str1, str2):
        count1 = [0 for _ in range(26)]
        count2 = [0 for _ in range(26)]
        i = 0
        while i < len(str1):
            count1 [str1[i] - 'a'] += 1
            i += 1
        i = 0
        while i < len(str2):
            count2 [str2[i] - 'a'] += 1
            i += 1
        result = ""
        for i in range(0, 26):
            j = 1
            while j <= min(count1 [i], count2 [i]):
                result += chr(('a' + i))
                j += 1
        print(result)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str1 = "geeks"
        str2 = "cake"
        GFG.longestString(str1, str2)
