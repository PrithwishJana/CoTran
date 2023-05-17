import math

class Solution:
    @staticmethod
    def max_element(A):
        max = Integer.MIN_VALUE
        i = 0
        while i < len(A):
            if max < A [i]:
                max = A [i]
            i += 1
        return max
    @staticmethod
    def SumDivPrime(A, n):
        max_val = (Solution.max_element(A)) + 1
        prime = [False for _ in range(max_val + 1)]
        for i in range(0, max_val + 1):
            prime [i] = True
        prime [0] = False
        prime [1] = False
        p = 2
        while p * p <= max_val:
            if prime [p] == True:
                for i in range(p * 2, max_val + 1, p):
                    prime [i] = False
            p += 1
        sum = 0
        for i in range(0, n):
            if prime [A [i]]:
                sum += A [i]
        for i in range(0, n):
            if prime [A [i]] and math.fmod(sum, A [i]) == 0:
                print("YES")
                return
        print("NO")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [1, 2, 3, 4, 5]
        n = len(A)
        Solution.SumDivPrime(A, n)
