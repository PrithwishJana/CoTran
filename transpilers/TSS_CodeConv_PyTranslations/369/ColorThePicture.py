import math

class ColorThePicture:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        pr = java.io.PrintWriter(System.out)
        t = int(br.readLine())
        while t != 0:
            ColorThePicture.solve(br, pr)
            t -= 1
        pr.flush()
        pr.close()
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void solve(java.io.BufferedReader br, java.io.PrintWriter pr) throws java.io.IOException
    def solve(br, pr):
        temp = br.readLine().split(" ")
        m = int(temp [0])
        n = int(temp [1])
        k = int(temp [2])
        sum = 0
        colors = [0 for _ in range(k)]
        temp = br.readLine().split(" ")
        for i in range(0, k):
            colors [i] = int(temp [i])
            sum += colors [i]
        flag = ColorThePicture.check(m, n, colors) or ColorThePicture.check(n, m, colors)
        pr.println("Yes" if flag else "No")
    @staticmethod
    def check(m, n, colors):
        count = 0
        set = java.util.HashSet()
        for i in colors:
            max = math.trunc(i / float(m))
            if max >= 2:
                count += max
                set.add(max)
        if count < n:
            return False
        if set.size() >= 2:
            return True
        if set.size() == 1:
            if set.contains(2):
                return True if math.fmod(n, 2) == 0 else False
            else:
                return True
        return True
