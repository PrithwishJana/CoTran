import math

class CodeForce:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        sb = StringBuilder()
        sr = br.readLine()
        ss = sr[0:len(sr) - 1]
        ch = sr[len(sr) - 1]
        list = []
        list.append('f')
        list.append('e')
        list.append('d')
        list.append('a')
        list.append('b')
        list.append('c')
        x = int(ss)
        m = math.fmod(x, 2)
        k = math.trunc((x - 1) / float(4))
        re = x - k
        total = 0
        total = 16 * k
        if m == 0:
            total += 7 + (list.index(ch) if ch in list else -1) + 1
        if m == 1:
            total += (list.index(ch) if ch in list else -1) + 1
        print(total)
