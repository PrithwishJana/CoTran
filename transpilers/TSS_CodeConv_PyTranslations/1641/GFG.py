class GFG:
    @staticmethod
    def even_or_odd(N):
        len = len(N)
        if N[len - 1] == '0' or N[len - 1] == '2' or N[len - 1] == '4' or N[len - 1] == '6':
            return ("Even")
        else:
            return ("Odd")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = "735"
        print(GFG.even_or_odd(N), end = '')
