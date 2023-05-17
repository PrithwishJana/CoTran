import math

class Main2:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException, InterruptedException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        testCases = sc.nextInt()
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (testCases -- > 0)
        while testCases  > 0:
            testCases -= 1
            activating = sc.nextInt()
            placing = sc.nextInt()
            input = sc.next()
            res = 0
            if placing >= activating:
                i = 0
                while i < len(input):
                    if input[i] == '0':
                        i += 1
                        continue
                    else:
                        res += activating
                        while i < len(input) and input[i] == '1':
                            i += 1
                    i += 1
                print(res)
            else:
                diff = math.trunc(activating / float(placing))
                firstOne = - 1
                i = 0
                while i < len(input):
                    if input[i] == '1':
                        firstOne = i
                        break
                    i += 1
                if firstOne == - 1:
                    print(0)
                else:
                    array = []
                    lastOne = firstOne
                    i = firstOne + 1
                    while i < len(input):
                        if input[i] == '1':
                            array.append(i - lastOne - 1)
                            lastOne = i
                        i += 1
                    res1 = 0
                    for i, unusedItem in enumerate(array):
                        first = array[i]
                        if first <= diff:
                            res1 += (first) * placing
                        else:
                            res1 += activating
                    res1 += activating
                    print(res1)
        testCases -= 1
