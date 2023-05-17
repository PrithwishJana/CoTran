import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def max_element(a):
        m = a [0]
        i = 0
        while i < len(a):
            m = max(a [i], m)
            i += 1
        return m
    @staticmethod
    def checkDivisors(a, n):
        X = GFG.max_element(a)
        b = list  ()
        i = 1
        while i * i <= X:
            if math.fmod(X, i) == 0:
                b.append(i)
                if math.trunc(X / float(i)) != i:
                    b.append(math.trunc(X / float(i)))
            i += 1
        if len(b) != n:
            return False
        Arrays.sort(a)
        b.sort()
        for i in range(0, n):
            if b[i] != a [i]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [8, 1, 2, 12, 48, 6, 4, 24, 16, 3]
        N = len(arr)
        if GFG.checkDivisors(arr, N):
            print("Yes")
        else:
            print("No")
