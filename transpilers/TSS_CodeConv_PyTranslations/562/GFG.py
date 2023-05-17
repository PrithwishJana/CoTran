class GFG:
    @staticmethod
    def findElement(arr, ranges, rotations, index):
        for i in range(rotations - 1, -1, -1):
            left = ranges [i][0]
            right = ranges [i][1]
            if left <= index and right >= index:
                if index == left:
                    index = right
                else:
                    index -= 1
        return arr [index]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5]
        rotations = 2
        ranges = [[ 0, 2 ], [ 0, 3 ]]
        index = 1
        print(GFG.findElement(arr, ranges, rotations, index))
