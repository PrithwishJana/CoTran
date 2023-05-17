class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def createHash(hash, maxElement):
        prev = 0
        curr = 1
        hash.add(prev)
        hash.add(curr)
        while curr < maxElement:
            temp = curr + prev
            hash.add(temp)
            prev = curr
            curr = temp
    @staticmethod
    def findFibonacciPair(n):
        hash = HashSet()
        GFG.createHash(hash, n)
        for i in range(0, n):
            if hash.contains(i) and hash.contains(n - i):
                print(str(i) + ", " + str(n - i) + "\n", end = '')
                return
        print("-1\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 90
        GFG.findFibonacciPair(N)
