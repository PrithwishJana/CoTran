class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fact(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countStrings(str, n):
        distinct_char = HashSet()
        for i in range(0, n):
            distinct_char.add(str[i])
        return GFG.fact(distinct_char.size())
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        n = len(str)
        print(GFG.countStrings(str, n))
