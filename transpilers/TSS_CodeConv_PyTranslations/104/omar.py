#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.abs
class omar:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = Scanner(System.in)
        size = input.nextInt()
        count = 0
        arr = [0 for _ in range(size)]
        for i in range(0, size):
            arr [i] = input.nextInt()
        Arrays.sort(arr)
        i = 1
        while i < size - 1:
            if arr [i] > arr [0] and arr [i] < arr [size - 1]:
                count += 1
            i += 1
        print(count)
