import math

class GFG:
    @staticmethod
    def bitonicGenerator(arr, n):
        evenArr = list  ()
        oddArr = list  ()
        for i in range(0, n):
            if math.fmod(i, 2) != 1:
                evenArr.append(arr [i])
            else:
                oddArr.append(arr [i])
        evenArr.sort()
        Collections.sort(oddArr, Collections.reverseOrder())
        i = 0
        for j, unusedItem in enumerate(evenArr):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: arr [i ++] = evenArr.get(j);
            arr [i ] = evenArr[j]
            i += 1
        for j, unusedItem in enumerate(oddArr):
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: arr [i ++] = oddArr.get(j);
            arr [i ] = oddArr[j]
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 5, 8, 9, 6, 7, 3, 4, 2, 0]
        n = len(arr)
        GFG.bitonicGenerator(arr, n)
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
