class GFG:
    @staticmethod
    def minimumValue(arr, n, k):
        Arrays.sort(arr)
        answer = 0
        for i in range(0, k):
            answer += arr [i] * arr [i]
        return answer * (2 * k - 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 21, 5, 3, 8]
        k = 3
        n = len(arr)
        print(GFG.minimumValue(arr, n, k), end = '')
