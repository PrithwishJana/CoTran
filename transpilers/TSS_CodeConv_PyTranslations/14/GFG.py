import math

class GFG:
    @staticmethod
    def checkIfPowerIsolated(num):
        input = num
        count = 0
        factor = [0 for _ in range(num + 1)]
        if math.fmod(num, 2) == 0:
            while math.fmod(num, 2) == 0:
                count += 1
                num = math.trunc(num / float(2))
            factor [2] = count
        i = 3
        while i * i <= num:
            count = 0
            while math.fmod(num, i) == 0:
                count += 1
                num = math.trunc(num / float(i))
            if count > 0:
                factor [i] = count
            i += 2
        if num > 1:
            factor [num] = 1
        product = 1
        i = 0
        while i < num + 1:
            if factor [i] > 0:
                product = product * factor [i] * i
            i += 1
        if product == input:
            print("Power-isolated Integer\n", end = '')
        else:
            print("Not a Power-isolated Integer\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.checkIfPowerIsolated(12)
        GFG.checkIfPowerIsolated(18)
        GFG.checkIfPowerIsolated(35)
