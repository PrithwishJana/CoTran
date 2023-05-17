class XeniaAndSpies:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        reader = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        input = reader.readLine().split(" ")
        m = int(input [1])
        s = int(input [2])
        f = int(input [3])
        maxT = - 1
        map = {}
        while m > 0:
            mth = reader.readLine().split(" ")
            k = int(mth [0])
            map[k] = []
            map[k].append(int(mth [1]))
            map[k].append(int(mth [2]))
            maxT = max(maxT, k)
            m -= 1
        actions = StringBuilder()
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final char M = (s < f) ? 'R' : 'L';
        M = 'R' if (s < f) else 'L'
        d = + 1 if (s < f) else - 1
        cur = s
        a = - 1
        b = - 1
        for t in range(1, maxT + 1):
            if t in map.keys():
                a = int(map[t][0])
                b = int(map[t][1])
            if t in map.keys() and ((cur >= a and cur <= b) or (cur + d >= a and cur + d <= b)):
                actions.append('X')
            else:
                actions.append(M)
                cur += d
            if cur == f:
                break
        while cur != f:
            actions.append(M)
            cur += d
        print(actions)
