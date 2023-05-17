class GFG:
    MAX = 10000
    s = HashSet()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        prime = [False for _ in range(GFG.MAX)]
        Arrays.fill(prime, True)
        prime [0] = False
        prime [1] = False
        p = 2
        while p * p < GFG.MAX:
            if prime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    prime [i] = False
                    i += p
            p += 1
        product = 1
        p = 2
        while p < GFG.MAX:
            if prime [p]:
                product = product * p
                GFG.s.add(product + 1)
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isEuclid(n):
        if n in GFG.s:
            return True
        else:
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
