import math

class GFG:
    @staticmethod
    def mean(mid, freq, n):
        sum = 0
        freqSum = 0
        for i in range(0, n):
            sum = sum + mid [i] * freq [i]
            freqSum = freqSum + freq [i]
        return sum / freqSum
    @staticmethod
    def groupedSD(lower_limit, upper_limit, freq, n):
        mid = [0 for _ in range(n)]
        sum = 0
        freqSum = 0
        sd = 0
        for i in range(0, n):
            mid [i] = (lower_limit [i] + upper_limit [i]) / 2
            sum = sum + freq [i] * mid [i] * mid [i]
            freqSum = freqSum + freq [i]
        sd = float(math.sqrt((sum - freqSum * GFG.mean(mid, freq, n) * GFG.mean(mid, freq, n)) / (freqSum - 1)))
        return sd
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        lower_limit = [50, 61, 71, 86, 96]
        upper_limit = [60, 70, 85, 95, 100]
        freq = [9, 7, 9, 12, 8]
        n = len(lower_limit)
        print(GFG.groupedSD(lower_limit, upper_limit, freq, n))
