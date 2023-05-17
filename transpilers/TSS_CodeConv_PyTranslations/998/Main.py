class GFG:
    set = TreeSet()
    @staticmethod
    def generateNumber(count, a, n, num, k):
        if count == k:
            GFG.set.add(num)
            return
        for i in range(0, n):
            GFG.generateNumber(count + 1, a, n, num + a [i], k)
    @staticmethod
    def printDistinctIntegers(k, a, n):
        GFG.generateNumber(0, a, n, 0, k)
        print("The" + " " + str(GFG.set.size()) + " " + "distinct integers are: ", end = '')
        print()
        i = GFG.set.iterator()
        while i.hasNext():
            print(i.next() + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 8, 17, 5]
        n = len(arr)
        k = 2
        GFG.printDistinctIntegers(k, arr, n)
