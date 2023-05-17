class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isVowel(c):
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return True
        return False
    @staticmethod
    def isVowelPrime(str, n):
        prime = [False for _ in range(n)]
        Arrays.fill(prime, True)
        prime [0] = False
        prime [1] = False
        p = 2
        while p * p < n:
            if prime [p] == True:
                for i in range(p * p, n, p):
                    prime [i] = False
            p += 1
        for i in range(0, n):
            if GFG.isVowel(str[i]) and not prime [i]:
                return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        n = len(str)
        if GFG.isVowelPrime(str, n):
            print("Yes")
        else:
            print("No")
