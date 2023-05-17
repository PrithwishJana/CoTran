class GFG:
    @staticmethod
    def maxProductSum(str, m):
        n = len(str)
        maxProd = Integer.MIN_VALUE
        maxSum = Integer.MIN_VALUE
        i = 0
        while i < n - m:
            product = 1
            sum = 0
            j = i
            while j < m + i:
                product = product * (str[j] - '0')
                sum = sum + (str[j] - '0')
                j += 1
            maxProd = max(maxProd, product)
            maxSum = max(maxSum, sum)
            i += 1
        print("Maximum Product = " + str(maxProd))
        print("Maximum Sum = " + str(maxSum))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "3675356291"
        m = 5
        GFG.maxProductSum(str, m)
