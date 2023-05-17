class PashaAndHamsters:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        is_ = java.io.InputStreamReader(System.in)
        br = java.io.BufferedReader(is_)
        dims = br.readLine().split(" ")
        total = int(dims [0])
        at = int(dims [1])
        pt = int(dims [2])
        vals = [False for _ in range(total)]
        as_ = br.readLine().split(" ")
        i = 0
        while i < len(as_):
            x = int(as_ [i])
            vals [x - 1] = True
            i += 1
        sb = StringBuffer()
        for i in range(0, total):
            sb.append(("1" if vals [i] else "2") + " ")
        print(sb)
