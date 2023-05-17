class GFG:
    bin = ["000", "001", "010", "011", "100", "101", "110", "111"]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxFreq(s):
        binary = ""
        i = 0
        while i < len(s):
            binary += GFG.bin [s[i] - '0']
            i += 1
        binary = binary[0:len(binary) - 1]
        count = 1
        prev = - 1
        i = 0
        j = 0
        i = binary.length() - 1
        while i >= 0:
            if binary[i] == '1':
                count = max(count, j - prev)
                prev = j
            i -= 1
            j += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        octal = "13"
        print(GFG.maxFreq(octal))
