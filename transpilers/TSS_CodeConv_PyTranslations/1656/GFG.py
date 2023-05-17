class GFG:
    MAX = 1000000
    prime = [False for _ in range(MAX + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        i = 0
        while i < GFG.MAX + 1:
            GFG.prime [i] = True
            i += 1
        GFG.prime [1] = False
        p = 2
        while p * p <= GFG.MAX:
            if GFG.prime [p] == True:
                i = p * 2
                while i <= GFG.MAX:
                    GFG.prime [i] = False
                    i += p
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findDiff(arr, n):
        min = GFG.MAX + 2
        max = - 1
        for i in range(0, n):
            if GFG.prime [arr [i]] == True:
                if arr [i] > max:
                    max = arr [i]
                if arr [i] < min:
                    min = arr [i]
        return - 1 if (max == - 1) else (max - min)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        n = 4
        arr = [1, 2, 3, 5]
        res = GFG.findDiff(arr, n)
        if res == - 1:
            print("No prime numbers", end = '')
        else:
            print("Difference is " + str(res))
