class BusesBetweenCities:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        pw = java.io.PrintWriter(System.out)
        st = java.util.StringTokenizer(br.readLine())
        a = int(st.nextToken())
        tA = int(st.nextToken())
        st = java.util.StringTokenizer(br.readLine())
        b = int(st.nextToken())
        tB = int(st.nextToken())
        timing = br.readLine()
        hrs = int(timing[0:2])
        mins = int(timing[3:])
        simDeparture = hrs * 60 + mins
        simArrival = simDeparture + tA
        counter = 0
        for i in range(300, 1440, b):
            busDeparture = i
            busArrival = i + tB
            if busDeparture >= simArrival or simDeparture >= busArrival:
                continue
            counter += 1
        pw.println(counter)
        pw.flush()
        pw.close()
