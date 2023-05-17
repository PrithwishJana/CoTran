class GFG:
    class pair:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.first = 0
            self.second = 0

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public pair(int first, int second)
        def __init__(self, first, second):
            self._initialize_instance_fields()

            self.first = first
            self.second = second
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def performQueries(A, q):
        n = len(A)
        pref_xor = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            pref_xor [i] = pref_xor [i - 1] ^ A [i - 1]
        for i in q:
            L = i.first
            R = i.second
            if L > R:
                temp = L
                L = R
                R = temp
            if L != R and pref_xor [R] == pref_xor [L - 1]:
                print("Yes")
            else:
                print("No")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        Arr = [1, 1, 2, 2, 1]
        q = [pair(1, 5), pair(1, 4), pair(3, 4)]
        GFG.performQueries(Arr, q)
