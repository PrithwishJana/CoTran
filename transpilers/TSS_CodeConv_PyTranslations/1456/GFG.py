class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def search(arr, n, x):
        front = 0
        back = n - 1
        while front <= back:
            if arr [front] == x or arr [back] == x:
                return True
            front += 1
            back -= 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
        x = 130
        n = len(arr)
        if GFG.search(arr, n, x):
            print("Yes", end = '')
        else:
            print("No", end = '')
