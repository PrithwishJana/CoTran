import math

class GFG:
    @staticmethod
    def multipleOfThree(K, dig0, dig1):
        sum = 0
        temp = math.fmod((dig0 + dig1), 10)
        sum = dig0 + dig1
        if K == 2:
            if math.fmod(sum, 3) == 0:
                return True
            else:
                return False
        sum += temp
        numberofGroups = math.trunc((K - 3) / float(4))
        remNumberofDigits = math.fmod((K - 3), 4)
        sum += (numberofGroups * 20)
        for i in range(0, remNumberofDigits):
            temp = math.fmod((2 * temp), 10)
            sum += temp
        if math.fmod(sum, 3) == 0:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        K = 5
        dig0 = 3
        dig1 = 4
        if GFG.multipleOfThree(K, dig0, dig1):
            print("Yes")
        else:
            print("No")
