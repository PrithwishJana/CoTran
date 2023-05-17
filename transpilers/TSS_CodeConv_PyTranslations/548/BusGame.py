import math

class BusGame:
    @staticmethod
    def canTake(xNeeded, xAvailable, yNeeded, yAvailable):
        if xNeeded > xAvailable:
            return False
        if yNeeded > yAvailable:
            return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        st = java.util.StringTokenizer(br.readLine())
        x = int(st.nextToken())
        y = int(st.nextToken())
        turn = 0
        while True:
            if math.fmod(turn, 2) == 0:
                if BusGame.canTake(2, x, 2, y):
                    x -= 2
                    y -= 2
                elif BusGame.canTake(1, x, 12, y):
                    x -= 1
                    y -= 12
                elif BusGame.canTake(0, x, 22, y):
                    y -= 22
                else:
                    print("Hanako")
                    return
            else:
                if BusGame.canTake(0, x, 22, y):
                    y -= 22
                elif BusGame.canTake(1, x, 12, y):
                    x -= 1
                    y -= 12
                elif BusGame.canTake(2, x, 2, y):
                    x -= 2
                    y -= 2
                else:
                    print("Ciel")
                    return
            turn += 1
