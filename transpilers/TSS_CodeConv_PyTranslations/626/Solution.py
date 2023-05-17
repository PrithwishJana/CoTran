import math

class Solution:
    def addStrings(self, num1, num2):
        sb = StringBuilder()
        carry = 0
        i = num1.length() - 1
        j = num2.length() - 1
        while i >= 0 or j >= 0 or carry == 1:
            x = 0 if i < 0 else num1[i] - '0'
            y = 0 if j < 0 else num2[j] - '0'
            sb.append(math.fmod((x + y + carry), 10))
            carry = math.trunc((x + y + carry) / float(10))
            i -= 1
            j -= 1
        return str(sb.reverse())
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        num1 = "11"
        num2 = "123"
        out = sObj.addStrings(num1, num2)
        print(out)
