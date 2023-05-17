import math

class GFG:
    @staticmethod
    def reduceString(s, l):
        count = 1
        steps = 0
        for i in range(1, l):
            if s[i] == s[i - 1]:
                count += 1
            else:
                steps += (math.trunc(count / float(2)))
                count = 1
        steps += math.trunc(count / float(2))
        return steps
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        l = len(s)
        print(GFG.reduceString(s, l))
