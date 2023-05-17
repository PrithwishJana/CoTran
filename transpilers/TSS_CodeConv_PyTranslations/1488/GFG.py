import math

class GFG:
    maxSize = int((1e5 + 5))
    isFib = [False for _ in range(maxSize)]
    prefix = [0 for _ in range(maxSize)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def digitSum(num):
        s = 0
        while num != 0:
            s = s + math.fmod(num, 10)
            num = math.trunc(num / float(10))
        return s
    @staticmethod
    def generateFibonacci():
        Arrays.fill(GFG.isFib, False)
        prev = 0
        curr = 1
        GFG.isFib [prev] = GFG.isFib [curr] = True
        while curr < GFG.maxSize:
            temp = curr + prev
            if temp < GFG.maxSize:
                GFG.isFib [temp] = True
            prev = curr
            curr = temp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def precompute(k):
        GFG.generateFibonacci()
        i = 1
        while i < GFG.maxSize:
            sum = GFG.digitSum(i)
            if GFG.isFib [sum] == True and math.fmod(sum, k) == 0:
                GFG.prefix [i] += 1
            i += 1
        i = 1
        while i < GFG.maxSize:
            GFG.prefix [i] = GFG.prefix [i] + GFG.prefix [i - 1]
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def performQueries(k, q, query):
        GFG.precompute(k)
        for i in range(0, q):
            l = query [i][0]
            r = query [i][1]
            cnt = GFG.prefix [r] - GFG.prefix [l - 1]
            print(str(cnt) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        query = [[ 1, 11 ], [ 5, 15 ], [ 2, 24 ]]
        k = 2
        q = len(query)
        GFG.performQueries(k, q, query)
