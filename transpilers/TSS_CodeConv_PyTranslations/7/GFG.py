class GFG:
    MAX = 1000000
    arr = list  ()
    prime = [False for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        i = 0
        while i < GFG.MAX:
            GFG.prime [i] = True
            i += 1
        p = 2
        while p * p < GFG.MAX:
            if GFG.prime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    GFG.prime [i] = False
                    i += p
            p += 1
        p = 2
        while p < GFG.MAX:
            if GFG.prime [p]:
                GFG.arr.append(p)
            p += 1
    @staticmethod
    def isPrimorialPrime(n):
        if not GFG.prime [n]:
            return False
        product = 1
        i = 0
        while product < n:
            product = product * GFG.arr[i]
            if product + 1 == n or product - 1 == n:
                return True
            i += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        n = 31
        if GFG.isPrimorialPrime(n):
            print("YES")
        else:
            print("NO")
