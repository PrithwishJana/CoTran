import math

class B999:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        t = int(br.readLine())
        str = br.readLine()
        for i in range(1, t + 1):
            if math.fmod(t, i) == 0:
                str = B999.reverse(str, i - 1)
        print(str)
    @staticmethod
    def reverse(str, last):
        arr = []
        i = 0
        while i < len(str):
            arr.append(str[i])
            i += 1
        counterUp = 0
        counterDown = last
        i = 0
        while i <= math.trunc(last / float(2)):
            Collections.swap(arr, counterUp, counterDown)
            counterUp += 1
            counterDown -= 1
            i += 1
        result = ""
        i = 0
        while i < len(str):
            result += arr[i]
            i += 1
        return result
