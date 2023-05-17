import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Integer.parseInt
class _1196A_ThreePilesOfCandies:
    @staticmethod
    def main(args):
        input = Scanner(System.in)
        test = parseInt(input.nextLine())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (test -- > 0)
        while test  > 0:
            test -= 1
            a = input.nextLong()
            b = input.nextLong()
            c = input.nextLong()
            result = math.trunc((a + b + c) / float(2))
            print(result)
        test -= 1
