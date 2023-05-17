class GFG:
    @staticmethod
    def kthString(n, k):
        total = 0
        i = 1
        while total < k:
            total = total + n - i
            i += 1
        first_y_position = i - 1
        second_y_position = k - (total - n + first_y_position)
        for j in range(1, first_y_position):
            print("x", end = '')
        print("y", end = '')
        j = first_y_position + 1
        while second_y_position > 1:
            print("x", end = '')
            second_y_position -= 1
            j += 1
        print("y", end = '')
        while j < n:
            print("x", end = '')
            j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 7
        GFG.kthString(n, k)
