class solution:
    prime = [False for _ in range(100006)]
    @staticmethod
    def SieveOfEratosthenes(n):
        for i in range(1, n + 1):
            solution.prime [i] = True
        solution.prime [1] = False
        p = 2
        while p * p <= n:
            if solution.prime [p] == True:
                for i in range(p * 2, n + 1, p):
                    solution.prime [i] = False
            p += 1
    @staticmethod
    def sortedArray(arr, n):
        solution.SieveOfEratosthenes(100005)
        v = list  ()
        for i in range(0, n):
            if solution.prime [arr [i]] == False:
                v.append(arr [i])
        v.sort()
        j = 0
        for i in range(0, n):
            if solution.prime [arr [i]] == True:
                print(str(arr [i]) + " ", end = '')
            else:
                print(str(v[j]) + " ", end = '')
                j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        arr = [100, 11, 500, 2, 17, 1]
        solution.sortedArray(arr, n)
