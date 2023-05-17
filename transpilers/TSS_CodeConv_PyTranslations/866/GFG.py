import math

class GFG:
    MAX = 1000000
    MOD = 10000007
    result = [0 for _ in range(MAX + 1)]
    fact = [0 for _ in range(MAX + 1)]
    @staticmethod
    def preCompute():
        GFG.fact [0] = 1
        GFG.result [0] = 1
        i = 1
        while i <= GFG.MAX:
            GFG.fact [i] = math.fmod(((math.fmod(GFG.fact [i - 1], GFG.MOD)) * i), GFG.MOD)
            GFG.result [i] = math.fmod(((math.fmod(GFG.result [i - 1], GFG.MOD)) * (math.fmod(GFG.fact [i], GFG.MOD))), GFG.MOD)
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def performQueries(q, n):
        GFG.preCompute()
        for i in range(0, n):
            print(GFG.result [q [i]])
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        q = [4, 5]
        n = len(q)
        GFG.performQueries(q, n)
