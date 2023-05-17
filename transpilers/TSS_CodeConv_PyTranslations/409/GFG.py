class GFG:
    @staticmethod
    def harmonicMean(arr, freq, n):
        sum = 0
        frequency_sum = 0
        for i in range(0, n):
            sum = sum + float(freq [i]) / arr [i]
            frequency_sum = frequency_sum + freq [i]
        return (frequency_sum / sum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = [13, 14, 15, 16, 17]
        freq = [2, 5, 13, 7, 3]
        n = len(num)
        print("{0:.4f}".format(GFG.harmonicMean(num, freq, n)))
