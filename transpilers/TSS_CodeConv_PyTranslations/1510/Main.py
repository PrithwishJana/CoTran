class Solution:
    @staticmethod
    def sum(n):
        if n == 1:
            return 2
        else:
            return (n * (n + 1) + Solution.sum(n - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print(Solution.sum(n))
