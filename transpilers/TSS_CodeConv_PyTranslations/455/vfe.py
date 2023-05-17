import math

class vfe:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        in_ = Scanner(System.in)
        x = in_.nextInt()
        y = in_.nextInt()
        list = []
        list.append(x)
        list.append(y)
        list.append(y - x)
        i = 2
        while not(list[i] == y and list[i - 1] == x or list[i] == 0 and list[i - 1] == 0):
            list.append(list[i] - list[i - 1])
            i += 1
        k = in_.nextInt()
        i -= 1
        k = math.fmod(k, i)
        if k == 0:
            k = i
        print(math.fmod(((math.fmod(list[k - 1], 1000000007)) + 1000000007), 1000000007))
