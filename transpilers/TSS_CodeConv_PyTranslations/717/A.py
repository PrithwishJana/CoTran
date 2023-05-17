import math

class A:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.in_ = None

    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        sb = StringBuilder()
        n = int(br.readLine())
        st = StringTokenizer(br.readLine())
        arr = [0 for _ in range(2 * n)]
        non_int = 0
        sum_before = 0
        sum = 0
        i = 0
        while i < 2 * n:
            num = float(st.nextToken())
            sum_before += num
            if num != math.floor(num):
                non_int += 1
            sum += math.floor(num)
            arr [i] = num
            i += 1
        max_sum = min(n, non_int) + sum
        min_sum = max(0, non_int - n) + sum
        ans = 0
        if min_sum > sum_before:
            ans = (min_sum - sum_before)
        elif max_sum < sum_before:
            ans = (sum_before - max_sum)
        else:
            x = sum_before - math.floor(sum_before)
            ans = min(1 - x, x)
        print("{0:.3f}".format(ans), end = '')
