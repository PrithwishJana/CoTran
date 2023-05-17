class GFG:
    @staticmethod
    def reverseorder(n):
        prime = [False for _ in range(n + 1)]
        for i in range(0, n):
            prime [i] = True
        p = 2
        while p * p <= n:
            if prime [p] == True:
                for i in range(p * 2, n + 1, p):
                    prime [i] = False
            p += 1
        for i in range(n, 1, -1):
            if prime [i] == True:
                print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 25
        print("Prime number in reverse order")
        if N == 1:
            print("No prime no exist in this range")
        else:
            GFG.reverseorder(N)
