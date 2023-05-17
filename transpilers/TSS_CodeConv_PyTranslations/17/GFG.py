import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def multiply(num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        if len1 == 0 or len2 == 0:
            return "0"
        result = [0 for _ in range(len1 + len2)]
        i_n1 = 0
        i_n2 = 0
        for i in range(len1 - 1, -1, -1):
            carry = 0
            n1 = num1[i] - '0'
            i_n2 = 0
            for j in range(len2 - 1, -1, -1):
                n2 = num2[j] - '0'
                sum = n1 * n2 + result [i_n1 + i_n2] + carry
                carry = math.trunc(sum / float(10))
                result [i_n1 + i_n2] = math.fmod(sum, 10)
                i_n2 += 1
            if carry > 0:
                result [i_n1 + i_n2] += carry
            i_n1 += 1
        i = len(result) - 1
        while i >= 0 and result [i] == 0:
            i -= 1
        if i == - 1:
            return "0"
        s = ""
        while i >= 0:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: s += (result [i --]);
            s += (result [i ])
            i -= 1
        return s
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str1 = "1235421415454545454545454544"
        str2 = "1714546546546545454544548544544545"
        if (str1[0] == '-' or str2[0] == '-') and (str1[0] != '-' or str2[0] != '-'):
            print("-", end = '')
        if str1[0] == '-' and str2[0] != '-':
            str1 = str1[1:]
        elif str1[0] != '-' and str2[0] == '-':
            str2 = str2[1:]
        elif str1[0] == '-' and str2[0] == '-':
            str1 = str1[1:]
            str2 = str2[1:]
        print(GFG.multiply(str1, str2))
