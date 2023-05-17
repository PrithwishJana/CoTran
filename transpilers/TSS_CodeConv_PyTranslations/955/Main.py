import math

class AP:
    @staticmethod
    def makeAP(arr, n):
        initial_term = 0
        common_difference = 0
        if n == 3:
            common_difference = arr [2] - arr [1]
            initial_term = arr [1] - common_difference
        elif (arr [1] - arr [0]) == arr [2] - arr [1]:
            initial_term = arr [0]
            common_difference = arr [1] - arr [0]
        elif (arr [2] - arr [1]) == (arr [3] - arr [2]):
            common_difference = arr [2] - arr [1]
            initial_term = arr [1] - common_difference
        else:
            common_difference = math.trunc((arr [3] - arr [0]) / float(3))
            initial_term = arr [0]
        for i in range(0, n):
            print(str(initial_term) + str(i * common_difference) + " ", end = '')
        print()
    @staticmethod
    def main(args):
        arr = [1, 3, 7]
        n = len(arr)
        AP.makeAP(arr, n)
