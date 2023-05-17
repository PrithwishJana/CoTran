import math

class MammothsGenomeDecoding:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        n = int(br.readLine())
        if math.fmod(n, 4) != 0:
            print("===")
            return
        themost = math.trunc(n / float(4))
        numA = 0
        numG = 0
        numC = 0
        numT = 0
        numQM = 0
        st = java.util.StringTokenizer(br.readLine())
        sb = StringBuffer(st.nextToken())
        i = 0
        while i < sb.length():
            if sb.charAt(i) == 'A':
                numA += 1
            elif sb.charAt(i) == 'G':
                numG += 1
            elif sb.charAt(i) == 'C':
                numC += 1
            elif sb.charAt(i) == 'T':
                numT += 1
            else:
                numQM += 1
            i += 1
        if numA > themost or numC > themost or numG > themost or numT > themost:
            print("===")
            return
        for j in range(0, numQM):
            i = 0
            while i < sb.length():
                if sb.charAt(i) == '?':
                    if numA < themost:
                        sb.replace(i, i + 1, "A")
                        numA += 1
                    elif numC < themost:
                        sb.replace(i, i + 1, "C")
                        pass
                        numC += 1
                    elif numG < themost:
                        sb.replace(i, i + 1, "G")
                        pass
                        numG += 1
                    elif numT < themost:
                        sb.replace(i, i + 1, "T")
                        pass
                        numT += 1
                i += 1
        print(sb)
