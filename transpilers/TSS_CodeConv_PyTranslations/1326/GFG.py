import math

class GFG:
    @staticmethod
    def countSubarraysof1and0(a, n):
        count1 = 0
        count0 = 0
        number1 = 0
        number0 = 0
        for i in range(0, n):
            if a [i] == 1:
                count1 += 1
            else:
                number1 += math.trunc((count1) * (count1 + 1) / float(2))
                count1 = 0
        for i in range(0, n):
            if a [i] == 0:
                count0 += 1
            else:
                number0 += math.trunc((count0) * (count0 + 1) / float(2))
                count0 = 0
        if count1 > 0:
            number1 += math.trunc((count1) * (count1 + 1) / float(2))
        if count0 > 0:
            number0 += math.trunc((count0) * (count0 + 1) / float(2))
        print("Count of subarrays of 0 only: " + str(number0))
        print("\nCount of subarrays of 1 only: " + str(number1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
        n = len(a)
        GFG.countSubarraysof1and0(a, n)
        pass
