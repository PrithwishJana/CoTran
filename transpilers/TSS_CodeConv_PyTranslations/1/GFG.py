import math

class GFG:
    MAX_CHAR = chr(26)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countFreq(str, freq, len):
        for i in range(0, len):
            freq [str[i] - 'a'] += 1
    @staticmethod
    def canMakePalindrome(freq, len):
        count_odd = 0
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            if math.fmod(freq [i], 2) != 0:
                count_odd += 1
            i += 1
        if math.fmod(len, 2) == 0:
            if count_odd > 0:
                return False
            else:
                return True
        if count_odd != 1:
            return False
        return True
    @staticmethod
    def findOddAndRemoveItsFreq(freq):
        odd_str = ""
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            if math.fmod(freq [i], 2) != 0:
                freq [i] -= 1
                odd_str = odd_str + chr((i + 'a'))
                return odd_str
            i += 1
        return odd_str
    @staticmethod
    def findPalindromicString(str):
        len = len(str)
        freq = [0 for _ in range(GFG.MAX_CHAR)]
        GFG.countFreq(str, freq, len)
        if not GFG.canMakePalindrome(freq, len):
            return "No Palindromic String"
        odd_str = GFG.findOddAndRemoveItsFreq(freq)
        front_str = ""
        rear_str = " "
        i = 0
        while chr(i) < GFG.MAX_CHAR:
            temp = ""
            if freq [i] != 0:
                ch = chr((i + 'a'))
                j = 1
                while j <= math.trunc(freq [i] / float(2)):
                    temp = temp + ch
                    j += 1
                front_str = front_str + temp
                rear_str = temp + rear_str
            i += 1
        return (front_str + odd_str + rear_str)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "malayalam"
        print(GFG.findPalindromicString(str))
