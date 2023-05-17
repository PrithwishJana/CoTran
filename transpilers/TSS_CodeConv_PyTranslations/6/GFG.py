class GFG:
    MAX = 10000
    arr = list  ()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        prime = [False for _ in range(GFG.MAX)]
        i = 0
        while i < GFG.MAX:
            prime [i] = True
            i += 1
        p = 2
        while p * p < GFG.MAX:
            if prime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    prime [i] = False
                    i += p
            p += 1
        p = 2
        while p < GFG.MAX:
            if prime [p]:
                GFG.arr.append(p)
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isEuclid(n):
        product = 1
        i = 0
        while product < n:
            product = product * GFG.arr[i]
            if product + 1 == n:
                return True
            i += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        n = 31
        if GFG.isEuclid(n):
            print("YES")
        else:
            print("NO")
        n = 42
        if GFG.isEuclid(n):
            print("YES")
        else:
            print("NO")
