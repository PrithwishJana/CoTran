class HelloWorld:
    @staticmethod
    def trapeziumPattern(num):
        firsthalf = 1
        secondhalf = (num * num) + 1
        numOfSpaces = 0
        for numOfLines in range(num, 0, -1):
            for numOfSpacesCounter in range(numOfSpaces, 0, -1):
                print(" ", end = '')
            for firstHalfCounter in range(1, numOfLines + 1):
                if firstHalfCounter == numOfLines:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: System.out.print((firsthalf ++));
                    print((firsthalf ), end = '')
                    firsthalf += 1
                else:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: System.out.print((firsthalf ++) + "*");
                    print(str(firsthalf ) + "*", end = '')
                    firsthalf += 1
            for secondHalfCounter in range(1, numOfLines + 1):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: System.out.print("*" + (secondhalf ++));
                print("*" + str(secondhalf ), end = '')
                secondhalf += 1
            print()
            numOfSpaces += 2
            secondhalf = (secondhalf - 1) - ((numOfLines - 1) * 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        HelloWorld.trapeziumPattern(3)
