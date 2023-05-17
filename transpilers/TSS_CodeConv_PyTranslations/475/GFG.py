import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def createHash(hash, maxElement):
        prev = 0
        curr = 1
        hash.add(prev)
        hash.add(curr)
        while curr <= maxElement:
            temp = curr + prev
            hash.add(temp)
            prev = curr
            curr = temp
    @staticmethod
    def gcdFibonacciFreq(arr, n):
        hash = HashSet()
        GFG.createHash(hash, Arrays.stream(arr).max().getAsInt())
        i = 0
        m = {}
        for i in range(0, n):
            if arr [i] in m.keys():
                m[arr [i]] = m[arr [i]] + 1
            else:
                m[arr [i]] = 1
        gcd = 0
        for it in m.entrySet():
            if hash.contains(it.getValue()):
                gcd = __gcd(gcd, it.getKey())
        return gcd
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        return a if b == 0 else GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 3, 6, 5, 6, 6, 5, 5]
        n = len(arr)
        print(GFG.gcdFibonacciFreq(arr, n), end = '')
