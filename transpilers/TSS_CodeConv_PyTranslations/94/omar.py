#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math.abs
class omar:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = Scanner(System.in)
        size = input.nextInt()
        min = 0
        max = 0
        arr = [0 for _ in range(size)]
        for i in range(0, size):
            arr [i] = input.nextInt()
        for i in range(0, size):
            if i == 0:
                min = abs(arr [i] - arr [i + 1])
                max = abs(arr [i] - arr [size - 1])
            elif i == size - 1:
                min = abs(arr [i] - arr [i - 1])
                max = abs(arr [i] - arr [0])
            elif i != 0 and i != size - 1:
                min = min(abs(arr [i] - arr [i - 1]), abs(arr [i] - arr [i + 1]))
                max = max(abs(arr [i] - arr [size - 1]), abs(arr [i] - arr [0]))
            print(str(min) + " " + str(max))
