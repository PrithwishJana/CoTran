import math

class GFG:
    @staticmethod
    def findTime(T, K):
        minutes = ((T[0] - '0') * 10 + T[1] - '0') * 60 + ((T[3] - '0') * 10 + T[4] - '0')
        minutes += K
        hour = math.fmod((math.trunc(minutes / float(60))), 24)
        min = math.fmod(minutes, 60)
        if hour < 10:
            print("0" + str(hour) + ":", end = '')
        else:
            print(str(hour) + ":", end = '')
        if min < 10:
            print("0" + str(min))
        else:
            print(min)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        T = "21:39"
        K = 43
        GFG.findTime(T, K)
