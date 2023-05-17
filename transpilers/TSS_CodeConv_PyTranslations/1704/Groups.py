import math

class Groups:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        Q = int(br.readLine())
        for i in range(0, Q):
            N = int(br.readLine())
            schedule = [[0 for _ in range(5)] for _ in range(N)]
            x = 0
            for j in range(0, N):
                line = br.readLine()
                sr = StringTokenizer(line)
                for k in range(0, 5):
                    schedule [x][k] = int(sr.nextToken())
                x += 1
            check = False
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#            outer :
            for j in range(0, 4):
                for k in range(j + 1, 5):
                    day1count = 0
                    day2count = 0
                    bothcount = 0
                    neither = 0
                    l = 0
                    while l < len(schedule):
                        if schedule [l][j] == 0 and schedule [l][k] == 0:
                            neither += 1
                        if schedule [l][j] == 1 and schedule [l][k] == 0:
                            day1count += 1
                        elif schedule [l][j] == 0 and schedule [l][k] == 1:
                            day2count += 1
                        elif schedule [l][j] == 1 and schedule [l][k] == 1:
                            bothcount += 1
                        l += 1
                    if neither > 0:
                        continue
                    elif day1count > math.trunc(len(schedule) / float(2)) or day2count > math.trunc(len(schedule) / float(2)):
                        continue
                    else:
                        check = True
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#                        break outer
            print("YES" if check else "NO")
