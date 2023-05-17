class GFG:
    @staticmethod
    def encodedChar(str, k):
        expand = ""
        temp = ""
        freq = 0
        i = 0
        while i < len(str):
            temp = ""
            freq = 0
            while i < len(str) and str[i] >= 'a' and str[i] <= 'z':
                temp += str[i]
                i += 1
            while i < len(str) and str[i] >= '1' and str[i] <= '9':
                freq = freq * 10 + str[i] - '0'
                i += 1
            for j in range(1, freq + 1):
                expand += temp
        if freq == 0:
            expand += temp
        return expand[k - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "ab4c12ed3"
        k = 21
        print(GFG.encodedChar(str, k))
