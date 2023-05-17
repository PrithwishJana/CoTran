class GFG:
    @staticmethod
    def get_maximum(s, a):
        n = len(s)
        for i in range(0, n):
            if s [i] - '0' < a [s [i] - '0']:
                j = i
                while j < n and (s [j] - '0' <= a [s [j] - '0']):
                    s [j] = chr(('0' + a [s [j] - '0']))
                    j += 1
                return str(s)
        return str(s)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "1337"
        a = [0, 1, 2, 5, 4, 6, 6, 3, 1, 9]
        print(GFG.get_maximum(s.toCharArray(), a))
